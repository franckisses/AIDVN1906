
from urllib import request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

# 构造请求对象
res_obj = request.Request('http://httpbin.org/get',headers=headers)
print(res_obj)
# 通过请求对象 生成响应对象
response = request.urlopen(res_obj)
# 获取响应内容
print(response.read().decode())

