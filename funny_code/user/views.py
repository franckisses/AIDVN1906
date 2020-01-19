from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from django.core.mail import send_mail
import base64
import random 
from django.conf import settings
from .weiboapi import OauthWeibo
from .models import  WeiboUser,UserProfile
import jwt
import hashlib
from django.db import transaction
import redis
from user_tasks.my_tasks import send_verify
from django_redis import get_redis_connection
# Create your views here.



class TestView(View):
    def get(self, request):
        print('test')
        r = redis.Redis()
        while True:
            try:
                with r.lock('shibw', blocking_timeout=3) as lock:
                    user = UserProfile.objects.get(username='shibw')
                    user.count += 1
                    user.save()
                break
            except Exception as e:
                print(e)
        return JsonResponse({'code':200,'data':'i am here!'})



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
            redis_conn = get_redis_connection('default')
            # 讲验证码存到redis中
            
            redis_conn.setex('user_%s'%email,60,code)

            # TODO 将生成的数据放入到redis中 
            try:
                send_verify.delay(email=email,code=code)
            except Exception as e:
                return JsonResponse({'code':103,'error':'send mail failed!'})
            return JsonResponse({'code':200,'data':'快去看邮件吧'})
        else:
            return JsonResponse({'code':100,'error':'code 有误！'})


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
        print(weibodata)
        access_token = weibodata.get('access_token')
        uid = weibodata.get('uid')

        try:    
            weibo_user = WeiboUser.objects.get(wuid=uid)
            # 1. 通过uid去查询是否绑定微博如果没有异常则已经绑定了
            #        发生异常没查到 那么没绑定给前端返回状态码 让用户绑定
        except Exception as e:
            WeiboUser.objects.create(wuid=uid,access_token=access_token)  
            return JsonResponse({'code':201,'uid':uid})
        else:
            # TODO 已经绑定了微博 返回token
            # 如果已经用微博登录了，但是没有绑定个人信息
            if weibo_user.uid:
                # 返回token
                # TODO 生成token 返回
                return JsonResponse({"code":200})
            else:
                return JsonResponse({'code':201,'uid':uid})


    def post(self,request):
        # 拿出表单的数据做绑定
        json_obj = request.body
        json_dict = json.loads(json_obj)
        # TODO  判断每一个值 是否为空
        username = json_dict.get('username')
        phone = json_dict.get('phone')
        email = json_dict.get('email')
        password = json_dict.get('password')
        uid = json_dict.get('uid')
        m = hashlib.md5()
        m.update(password.encode())
        password_m = m.hexdigest()
        # 存储用户信息以及微博信息
        try:
            with transaction.atomic():
                # 存储个人信息表：
                user = UserProfile.objects.create(
                    username=username,
                    phone=phone,
                    password=password_m,
                    email=email
                )
                weibo_user  = WeiboUser.objects.get(wuid=uid)
                weibo_user.uid = user
                weibo_user.save()
        except Exception as e:
            return JsonResponse({'code':205,'error':'create user failed'})
        # TODO  生成token返回
        return JsonResponse({'code':200}) 
        


