
from django.conf import settings 
from urllib.parse import urlencode
import requests # pip3 install requests

class OauthWeibo:

    def __init__(self):
        # 网页应用app key
        self.client_id = settings.APP_KEY
        # 网页应用的 app secret
        self.client_secret = settings.APP_SECRET
        # 重定向地址
        self.redirect_uri = settings.REDIRECT_URI


    def get_weibo_url(self):
        """
        该方法用来获取微博登录页面地址
        """
        base_url = 'https://api.weibo.com/oauth2/authorize?'
        params = {
            'response_type':'code',
            'client_id':self.client_id,
            'redirect_uri':self.redirect_uri
        }   
        query_string = urlencode(params)
        # ?name=1&age=2
        weibourl = base_url+query_string
        return weibourl


    def get_access_token(self,code):
        """
        通过code 获取access token 
        """
        base_url = 'https://api.weibo.com/oauth2/access_token'
        data = {
            'client_id':self.client_id,
            'client_secret':self.client_secret,
            'grant_type':'authorization_code',
            'code':code,
            'redirect_uri':self.redirect_uri
        }      # requests
        try:
            response = requests.post(base_url,data=data)
        except Exception as e:
            raise ValueError('请求异常')
        