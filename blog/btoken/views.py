from django.shortcuts import render
from django.http import JsonResponse
import json
import hashlib

from user.models import UserProfile
from django.conf import settings
# Create your views here.


def tokens(request):
    # http://127.0.0.1:8000/v1/tokens
    # POST 
    # params  username password
    if not request.method == 'POST':
        return JsonResponse({
            'code':208,
            'error':'request method is not allowed!'
            })
    #　获取数据
    json_obj = request.body
    if not json_obj:
        return JsonResponse({'code':201,'error':'please give me data!'})
    # 生成字典
    json_dict = json.loads(json_obj)
    username = json_dict.get('username',None)
    password = json_dict.get('password',None)
    if not username:
        return JsonResponse({'code':210,'eroor':'please give me username!'})
    if not password:
        return JsonResponse({'code':211,'error':'please give me password!'})
    user  = UserProfile.objects.filter(username=username)
    if not user:
        return JsonResponse({'code':212,'error':'username or password is wrong!'})
    user  = user[0]
    m = hashlib.md5()
    m.update(password.encode())
    if m.hexdigest() != user.password:
        return JsonResponse({'code':212,'error':'用户密码错误！'})
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
    # 
    payload['exp'] = time.time() + exp
    return jwt.encode(payload,settings.TOKEN_KEYS,algorithm='HS256')

