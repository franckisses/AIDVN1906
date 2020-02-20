
import requests
import time
from fake_useragent import UserAgent
from hashlib import md5
import random 

class YouDaoSpider:
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': '_ntes_nnid=b657d7390ec9879ded9d7a8d330de789,1580460208201; OUTFOX_SEARCH_USER_ID_NCOO=1360812747.7288582; OUTFOX_SEARCH_USER_ID="-688915196@10.108.160.18"; JSESSIONID=aaadA4iSHuevc6PKYPHbx; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1582206448886',
            'Referer': 'http://fanyi.youdao.com/'
        }
        self.proxies = {
            'http':'http://xxxxx',
            'https':'https://xxxxx'
        }

    def get_md5(self,parmas):
        #主要用来生生成md5加密参数
        s = md5()
        s.update(parmas.encode())
        return s.hexdigest()
    # 生成加密参数
    def __get_secret_params(self,words):
        # 生成四个加密参数
        ts = str(int(time.time() * 1000))
        bv = 'e77fdbd7d7eb6dba8e3f74b35481a113'
        salt = ts + str(random.randint(0,9))
        origin_sign = "fanyideskweb" + words + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
        sign = self.get_md5(origin_sign)
        print(sign)
        return ts,bv,salt,sign

    def translate_words(self):
        print('欢迎使用人工智能翻译:')
        # TODO 检查输入
        user_input = input('请输入您要翻译的单词：')
        ts,bv,salt,sign = self.__get_secret_params(user_input)
        data = {
            'i': user_input,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': bv,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        response = requests.post(url=self.url,data=data,headers=self.headers)
        print(response.status_code)
        html = response.json()
        print(type(html))
        print('翻译结果是:',html['translateResult'][0][0]['tgt'])



if __name__ == "__main__":
    youdao = YouDaoSpider()
    youdao.translate_words()
