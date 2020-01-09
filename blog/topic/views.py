from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import Topic
from utils.loging_check import loging_check,get_user_by_request
from user.models import UserProfile
from message.models import Message
# Create your views here.


class TopicView(View):

    def get(self, request,username):
        """
        用户登录  
            获取全量数据 公开的私有的
            获取部分数据 ？tec no-tec
        用户未登录
            获取全量的公开的数据
            获取部分数据 tec no-tec
            ＃获取博客详情页面内容：
            http://127.0.0.1:8000/v1/topics/franck?t_id=1   
        """
        authors = UserProfile.objects.filter(username=username)
        if not authors:
            return JsonResponse({'code':303,'error':'user not existed!'})
        author = authors[0]
        visitor = get_user_by_request(request)
        visitor_name = None
        if visitor:
            visitor_name = visitor.username
        t_id = request.GET.get('t_id',None)
        # TODO 判断用传递的博客ID是否存在 
        if t_id:
            id = int(t_id)
            # 如果 用户访问自己的博客，不用去查看是否否公开
            #       访客来访问的话，那么我们要对权限进行验证
            is_self = False
            if username == visitor_name:
                is_self = True
                # 认为是登录的
                try:
                    author_topic = Topic.objects.get(id=t_id)
                except Exception as e:
                    return JsonResponse({'code':307,'error':'no such topic'})
            else:
                # 认为非登录的状态
                try:
                    author_topic = Topic.objects.get(id=t_id,limit='public')
                except Exception as e:
                    return JsonResponse({'code':308,'error':'you cant read it！'})
            res = make_topic_res(author,author_topic,is_self)
            return JsonResponse(res)
        else:
            category = request.GET.get('category',None)
            if category in ['tec','no-tec']:
                if username == visitor_name:
                    topics = Topic.objects.filter(author_id=username,category=category)
                else:
                    topics = Topic.objects.filter(author_id=username,category=category,limit='public')        
            else:
                # 判断用户是否是一致：
                if username == visitor_name:
                    topics = Topic.objects.filter(author_id=username)
                else:
                    topics = Topic.objects.filter(author_id=username,limit='public')        
            res = make_topics(author,topics)
            return JsonResponse(res)
        
    @loging_check
    def post(self, request,username):
        json_obj = request.body
        if not json_obj:
            return JsonResponse({'code':301,'error':'please give me data'})
        json_dict = json.loads(json_obj)
        # TODO 自己去判断每一项前端传递的 数据
        title = json_dict.get('title')
        content = json_dict.get('content')
        content_text = json_dict.get('content_text')
        introduce = content_text[:30]
        limit = json_dict.get('limit',None)
        category = json_dict.get('category')
        try:
            Topic.objects.create(
                title=title,
                content=content,
                introduce=introduce,
                limit=limit,
                category=category,
                author=request.user
            )
        except Exception as e:
            print('用户创建博客失败：',e)
            return JsonResponse({'code':302,'error':'create blog failed!'})
        return JsonResponse({'code':200,'username':request.user.username})

    @loging_check
    def delete(self,request,username):
        """
        博客删除功能接口
        http://127.0.0.1:8000/v1/topics/username?topic_id=x
        """
        username_token = request.user.username
        if username != username_token:
            return JsonResponse({'code':304,'error':'you cant do that!'})
        topic_id = request.GET.get('topic_id',None)
        # TODO 检查前段传递的查询字符串是否存在
        try:
            topic = Topic.objects.get(id=topic_id)
        except Exception as e:
            return JsonResponse({'code':305,'error':'blog is not existed!'})
        #检查是否为自己的博客：
        if topic.author.username != username:
            return JsonResponse({'code':306,'error':'you can do that!'})
        #　TODO : 可以在博客表中再天剑一个字段：　is_active  True/ False 
        topic.delete()
        return JsonResponse({'code':200,'data':'删除成功'})


def make_topics(author,topics):
    import time
    res = {'code':200,'data':{}}
    data = {}
    topics_list = []
    for topic in topics:
        d = {}
        d['id'] = topic.id
        d['title'] = topic.title
        d['category'] = topic.category
        d['author'] = author.username
        d['introduce'] = topic.introduce
        d['created_time'] = topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
        topics_list.append(d)
    data['topics'] = topics_list
    data['nickname'] =author.nickname
    res['data'] = data

    return res


def  make_topic_res(author,author_topic,is_self):
    """
    组织博客详情页面的数据
    """
    if is_self:
        # 查询博主本人的博客
        #　获取前一篇博客：lt ---less than 
        last_topic = Topic.objects.filter(
            id__lt=author_topic.id,author=author).last()
        # 获取下一篇博客：
        next_topic = Topic.objects.filter(
            id__gt=author_topic.id,author=author).first()
    else:
        # 查询博主本人的博客
        #　获取前一篇博客：lt ---less than 
        last_topic = Topic.objects.filter(
            id__lt=author_topic.id,author=author,limit='public').last()
        # 获取下一篇博客：
        next_topic = Topic.objects.filter(
            id__gt=author_topic.id,author=author,limit='public').first()
    # 判断是否存在前一篇博客和后一篇博客
    if next_topic:
        next_id = next_topic.id
        next_title = next_topic.title
    else:
        next_id = None
        next_title = None
    if last_topic:
        last_id = last_topic.id
        last_title = last_topic.title
    else:
        last_id = None
        last_title = None
    all_message = Message.objects.filter(
        topic=author_topic).order_by('-created_time')

    msg_list = []
    reply_dict = {}
    msg_count = 0
    for msg in all_message:
        if msg.parent_message == 0:
            msg_count += 1
            msg_list.append({
                'id':msg.id,
                'content':msg.content,
                'publisher':msg.publisher.username,
                'created_time':msg.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                'publisher_avatar':str(msg.publisher.avatar),
                'reply':[] # {1:{}}
            })
        else:
            reply_dict.setdefault(msg.parent_message,[])# {1:{}}
            reply_dict[msg.parent_message].append({
                'id':msg.id,
                'content':msg.content,
                'publisher':msg.publisher.username,
                'created_time':msg.created_time.strftime('%Y-%m-%d %H:%M:%S'),
                'publisher_avatar':str(msg.publisher.avatar)
            })
        for _msg in msg_list:
            if _msg['id'] in reply_dict:
                _msg['reply'] = reply_dict[_msg['id']]
        # 序列化功能

    #  组织前端数据
    res = {'code':200,'data':{}}
    res['data']['nickname'] =author.nickname
    res['data']['title'] = author_topic.title
    res['data']['introduce'] = author_topic.introduce
    res['data']['category'] = author_topic.category
    res['data']['content'] = author_topic.content
    res['data']['author'] =author.nickname
    res['data']['created_time'] = author_topic.created_time.strftime('%Y-%m-%d %H:%M:%S')
    res['data']['last_id'] = last_id
    res['data']['last_title'] = last_title
    res['data']['next_id'] = next_id
    res['data']['next_title'] = next_title
    ### 留言相关的写为空
    res['data']['messages'] = msg_list
    res['data']['messages_count'] = msg_count
    print(res)
    return res  


# "messages": [{
# 		"id": 1,
# 		"content": "<p>写得不错啊，大哥<br></p>",
# 		"publisher": "guoxiaonao",
# 		"publisher_avatar": "avatar/头像 2.png",
#         "created_time": "2019-06-03 07:52:02"
# 		"reply": [{
# 			"publisher": "guoxiaonao",
# 			"publisher_avatar": "avatar/头像 2.png",
# 			"created_time": "2019-06-03 07:52:16",
# 			"content": "谢谢您的赏识",
# 			"msg_id": 2
# 		},
#         {
# 		"id": 3,
# 		"content": "<p>写得不错啊，大哥<br></p>",
# 		"publisher": "guoxiaonao",
# 		"publisher_avatar": "avatar/头像 2.png",
#         "created_time": "2019-06-03 07:52:02"
# 		"reply": [{
# 			"publisher": "guoxiaonao",
# 			"publisher_avatar": "avatar/头像 2.png",
# 			"created_time": "2019-06-03 07:52:16",
# 			"content": "谢谢您的赏识",
# 			"msg_id": 4
#		}],
#	}
