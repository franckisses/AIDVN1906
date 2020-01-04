from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import Topic
from utils.loging_check import loging_check
# Create your views here.


class TopicView(View):
    def get(self, request,username):
        return JsonResponse({'code':200})
    
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
                # author_id = request.user.id
            )
        except Exception as e:
            print('用户创建博客失败：',e)
            return JsonResponse({'code':302,'error':'create blog failed!'})
        return JsonResponse({'code':200,'username':request.user.username})