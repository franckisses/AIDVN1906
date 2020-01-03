
from django.http import JsonResponse
from django.conf import settings
from functools import wraps
from user.models import UserProfile
import jwt

def loging_check(func):
    @wraps(func)
    def wrapper(self,request,*args,**kwargs):
        # 登录验证：
        # 获取token
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return JsonResponse({'code':215,'error':'please login'})
        try:
            res = jwt.decode(token,settings.TOKEN_KEYS,algorithms='HS256')
        except jwt.ExpiredSignatureError as e:
            print(e)
            return JsonResponse({'code':216,'error':'please login'})
        except Exception as e:
            print(e)
            return JsonResponse({'code':217,'error':'please login'})
        username =  res['username'] # res payload 字典
        user = UserProfile.objects.get(username=username)
        request.user = user
        return func(self,request,*args,**kwargs)
    return wrapper