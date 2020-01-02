from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
import hashlib

from .models import UserProfile

# Create your views here.

class UserRegisterView(View):
    """
    通过类视图来写view
    """
    def get(self,request):
        pass

    def post(self,request):
        """
        1. 获取浏览器前段传递的数据
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
def make_token(payload,exp=24*3600):
    import jwt
    import time 
    key = '123321' 
    payload['exp'] = time.time() + exp
    return jwt.encode(payload,keys,algorithm='HS256')