
from urllib import request
import random

UA_LIST = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser) Green Browser',
    'User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18'
]

headers = {
    'User-Agent': random.choice(UA_LIST)
}

# 构造请求对象
res_obj = request.Request('http://httpbin.org/get',headers=headers)
print(res_obj)
# 通过请求对象 生成响应对象
response = request.urlopen(res_obj)
# 获取响应内容
print(response.read().decode())

# fake_useragent
