from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from utils.loging_check import loging_check
import json
from topic.models import Topic
from user.models import UserProfile
from .models import Message
# Create your views here.

class MessageView(View):
    """
    发表博客留言功能
    """
    @loging_check
    def post(self,request,topic_id):
        """
        发表评论功能　接口
        http://127.0.0.1:8000/v1/messages/<topic_id>
        """
        # TODO 　检查用户是否一致
        json_obj = request.body
        json_dict = json.loads(json_obj)
        # TODO 自己检查内容是否存在
        content = json_dict.get('content',None)
        parent_message = json_dict.get('parent_id',0)
        try:
            topic = Topic.objects.get(id=topic_id)
        except Exception as e:
            return JsonResponse({'code':401,'error':'blog is not existed!'})
        # 判断博客是否为私有的
        if topic.limit == 'private':
            return JsonResponse({'code':402,'error':'you cant comment it!'})

        
        try:
            Message.objects.create(
                content=content,
                publisher=request.user,
                topic = topic,
                parent_message = parent_message,
            )
        except Exception as e:
            return JsonResponse({'code':403,'error':'create comments failed!！'})
        return JsonResponse({'code':200,'data':{}})