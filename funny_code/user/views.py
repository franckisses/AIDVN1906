from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.core.mail import send_mail
import base64
import random 
from django.conf import settings
from .weiboapi import OauthWeibo
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
            # 发送邮箱验证码：
            # TODO code 一般存在redis 数据库中设置一个时间。
            code = '%d'%random.randint(100000,999999)   
            subject = 'AID1906邮箱验证码'

            html_message = '<p>尊敬的学员，您好：</p>'\
                '<p>欢迎来到老龚课堂</p>'\
                '<p>您的邮箱为：%s,您的邮箱验证码为:<b>%s</b>,该验证码10分钟之内有效</p>'%(email,code)
            try:
                send_mail(subject,'',settings.EMAIL_FROM,[email],
                html_message=html_message)
            except Exception as e:
                return JsonResponse({'code':103,'error':'send mail failed!'})
            return JsonResponse({'code':200,'data':'快去看邮件吧'})
        else:
            return JsonResponse({'code':100,'error':'code 有误！'})

"""
# https://api.weibo.com/oauth2/authorize?
client_id=YOUR_CLIENT_ID&
response_type=code&
redirect_uri=YOUR_REGISTERED_REDIRECT_URI
"""

class WeiboUrlView(View):
    def get(self,requset):
        # http://127.0.0.1:8000/v1/users/weibo
        try:
            oauth = OauthWeibo()
            oauth_url = oauth.get_weibo_url()
        except Exception as e:
            return JsonResponse({'code':203,'error':'something error'})
        return JsonResponse({'code':200,'oauth_url':oauth_url})

class WeiboUserView(View):
    def get(self,request):
        # TODO  判断前段传递的code
        code = request.GET.get('code',None)
        try:
            oauth = OauthWeibo()
            weibodata = oauth.get_access_token(code)
        except Exception as e:
            return JsonResponse({'code':204,'error':'cant get access token'})