


# 第一步 找请求的地址
# 第二步 模拟http发送请求
# 第三步 通过请求返回之后的响应来获取网页中的有效信息

import random
from fake_useragent import UserAgent
HEADERS_LIST = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser) Green Browser',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18'
]

from urllib import parse,request

def build_url():
    """
    生成访问的url
    :return:
    """
    keyword = input('您好呀,想查点啥呢?')
    params = parse.quote(keyword)
    url = 'https://www.baidu.com/s?wd='+params
    return url

def get_page(current_url):
    """
    模拟浏览器发送请求
    """
    res_obj = request.Request(
        current_url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'Upgrade-Insecure-Requests': 1,
            'Cookie': 'BIDUPSID=14F379E3B5054EF675336D32DA98A824; PSTM=1569211452; BD_UPN=12314353; BAIDUID=14F379E3B5054EF675336D32DA98A824:SL=0:NR=10:FG=1; sug=0; sugstore=1; ORIGIN=0; bdime=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1446_21127_30490_30499; BDSFRCVID=Io-OJeC62uOSXRRu5sJy2RXcRoABp-7TH6aofXrB4XBwpaXVPzn6EG0PDx8g0KubhO-qogKK0mOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJCJ_KPbJKK3fP36qRbqhRteKlbb5R3KHD7XVKJ5Lp7keq8CDR5kyt0b3h_tWh0ttHrv3Mo_tMn5Sxj2y5jHhPtiyfrpKfuH0eTwW66o2DnpsIJMybAWbT8U5f5U3RIOaKviaKJEBMb1MlvDBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6j3DH_8Jj-HfKrBstJXbnnoD6rmbtOhq4tHeUrrtURZ5mAqot5vLMnCV4KGKn8WDlDR-n5y3xjjHRvnaIQqabQiql_mWM5bK-_R3R3E2j543bRTKPPy5KJvfJodXIcahP-UyN3LWh37Je3lMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafD_MhDKwD6tKePDqql38-PvyatoJ0RbaHJO_bpTvqfnkbfJBDlo9QhvNLjItQhcXtfoiHUovLf52qj-7yajK2-5v-euJhpo5-njiSxJuh6jpQT8rQhAOK5OibCr3256hab3vOIJzXpO1jxPzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksD-FtqtJHKbDD_IDbJfK; delPer=0; BD_CK_SAM=1; PSINO=2; COOKIE_SESSION=1495_11_6_7_63_56_0_3_6_4_0_4_0_5893_0_0_1579526675_1579527755_1579529195%7C9%236026_22_1579527700%7C6; H_PS_645EC=66c4pP%2BNP34FGLec1xE9i4qyRcKopKJz8Us1oVzGDg%2FYMLATMzlCnoJnhzs'
        }
    )
    response = request.urlopen(res_obj)
    return response



def parse_page(response):
    """
    网页解析
    :return:
    """
    print(response.read().decode())

if __name__ == '__main__':
    url = build_url()
    print(url)
    response = get_page(url)
    parse_page(response)
