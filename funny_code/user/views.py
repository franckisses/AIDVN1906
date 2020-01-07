from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
# Create your views here.
class EmailView(View):
    """邮箱验证的接口"""
    def post(self,request):
        # TODO 需要判断前段传过来的每一个参数
        json_obj = request.body
        json_dict = json.loads(json_obj)
        email = json_dict.get('email') 
        send_type = json_dict.get('code')
        # 当发送类型为１　发送邮箱激活链接
        # 当发送类型为２　发送邮箱验证码
        if　int(send_type) == 1:
            pass
        elif int(send_type) == 2:
            pass
        else:
            return JsonResponse({'code':100,'error':'code 有误！'})