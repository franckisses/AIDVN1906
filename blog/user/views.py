from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
import hashlib

from btoken.views import make_token
from .models import UserProfile
from utils.loging_check import loging_check

# Create your views here.

class UserRegisterView(View):
    """
    通过类视图来写view
    """
    def get(self,request,username=None):
        # 判断前端是否传递用户名
        if username:
            try:
                user = UserProfile.objects.get(username=username)
            except Exception as e:
                print('GET方法获取用户名',e)
                user = None
            if not user:
                return JsonResponse({'code':214,'error':'user not existed!'})
            # 获取前端传递的查询字符串：
            if request.GET.keys():
                data = {}
                for s in request.GET.keys(): # s ---str
                    if hasattr(user,s):
                        each_data = getattr(user,s)
                        if 'avatar' == s:
                            data[s] = str(each_data)
                        else:
                            data[s] = each_data
                return JsonResponse({
                    'code':200,
                    'username':username,
                    'data': data
                })
            # 没有查询字符串，返全量数据
            return JsonResponse({
                'code':200,
                'username':user.username,
                'data':{
                    'nickname':user.nickname,
                    'avatar':str(user.avatar),
                    'sign':user.sign,
                    'info':user.info
                }
            })
        else:
            return JsonResponse({'code':213,'error':'please give me username'})
        

    def post(self,request):
        """
        1. 获取浏览器前端传递的数据
        2. 验证前端传递的数据。
        3. 判断用户是不是在我们数据库中存在。
        4. 判断用户密码是否合法。对密码进行处理
        5. 创建用户。生成ｔｏｋｅｎ.返回给前端。
        """
        json_obj = request.body
        if not json_obj:
            return JsonResponse({'code':201,'error':'no content!'})
        json_dict = json.loads(json_obj)

        # 验证用户名
        username = json_dict.get('username',None)
        if not username:
            return JsonResponse({'code':202,'error':'no username'})
        # 获取邮箱。获取密码
        email = json_dict.get('email',None)
        if not email:
            return JsonResponse({'code':203,'error':'no email'})
        password_1 = json_dict.get('password_1',None)
        password_2 = json_dict.get('password_2',None)
        if not password_1 or not password_2:
            return JsonResponse({'code':204,'error':'no password'})
        # 密码１　和　密码２　需要一致
        if password_1 != password_2:
            return JsonResponse({'code':205,'error':'different password!'})
        old_user = UserProfile.objects.filter(username=username)
        if old_user:
            return JsonResponse({'code':206,'error':'user already existed!'})
        m = hashlib.md5()
        m.update(password_1.encode())
        sign = info = " "
        try:
            UserProfile.objects.create(
                username=username,
                nickname=username,
                password=m.hexdigest(),
                sign=sign,
                info=info, 
                email=email
            )
        except Exception as e:
            # logging
            return JsonResponse({'code':207,'error':'server is busy!'})
            # 生成token
        token = make_token({'username':username})
        return JsonResponse({
            'code':200,
            'username':username,
            'data':{
                'token':token.decode()
            }
            })

    @loging_check
    def put(self,request,username):
        # PUT http://127.0.0.1:8000/v1/users/username
        #更新用户个人数据
        # 后端接口中传递的数据中的username 和token中取来的username做一次校验
        token_username = request.user.username 
        if username != token_username:
            return JsonResponse({'code':217,'error':'requset error'})
        json_obj = request.body
        if not json_obj:
            return JsonResponse({'code':218,'error':'please give data!'})
        json_dict = json.loads(json_obj)
        info = json_dict.get('info',None)
        sign = json_dict.get('sign',None)
        nickname = json_dict.get('nickname',None)
        if not info or not sign or not nickname:
            return JsonResponse({'code':219,'error':'i need more data!'})
        user = request.user
        try:
            user.sign = sign
            user.info = info
            user.nickname = nickname
            user.save()
        except Exception as e:
            return JsonResponse({'code':220,'error':'user info modify failed!'})
        return JsonResponse({'code':200,'username':user.username})


class UserAvatarView(View):

    @loging_check
    def post(self,request,username):
        # TODO 检查username 是否一致
        #  获取用户头像二进制文件
        avatar = request.FILES.get('avatar',None)
        return JsonResponse({'code':222})
        if not avatar:
            return JsonResponse({'code':221,'error':'please give me avatar!'})
        try:
            request.user.avatar = avatar
            request.user.save() 
        except Exception as e:
            return JsonResponse({'code':222,'error':'modify avatar failed!'})
        return JsonResponse({'code':200,'username':request.user.username})