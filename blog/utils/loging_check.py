
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



def get_user_by_request(request):
    """
    通过reuqest 判断登录状态： 获取用户名
    """
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    try:
        res = jwt.decode(token,settings.TOKEN_KEYS,algorithms='HS256')
    except Exception as e:
        return None
    username = res['username']
    try:
        user = UserProfile.objects.get(username=username)
    except Exception as e:
        return None
    return user