from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.core.mail import send_mail
import base64
import random 
from django.conf import settings
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
        if int(send_type) == 1:
            active_code = email +'.'+ "%d"%random.randint(100000,999999)
            m = base64.urlsafe_b64encode(active_code.encode()).decode()
            active_url = 'http://127.0.0.1/v1/users/active?code='+m
            subject = 'AID1906激活邮件'
            message = '点击发送激活链接' + active_url
            from_email = settings.EMAIL_FROM

            try:
                send_mail(subject,message,from_email,[email])
            except Exception as e:
                print(e)
                return JsonResponse({'code':102,'error':'send mail failed!'})
            return JsonResponse({'code':200,'data':'快去看邮件吧！'})
        elif int(send_type) == 2:
            pass
        else:
            return JsonResponse({'code':100,'error':'code 有误！'})