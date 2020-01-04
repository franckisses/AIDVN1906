from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import Topic
from utils.loging_check import loging_check,get_user_by_request
from user.models import UserProfile
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
        """
        authors = UserProfile.objects.filter(username=username)
        if not authors:
            return JsonResponse({'code':303,'error':'user not existed!'})
        author = authors[0]
        visitor = get_user_by_request(request)
        visitor_name = None
        if visitor:
            visitor_name = visitor.username
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