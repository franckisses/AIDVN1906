
import requests

# requests 
# sudo pip3 install requests
url = 'http://httpbin.org/get'
headers = {'User-Agent':'Mozilia/5.0'}

response = requests.get(url,headers=headers)

# 查看响应码
print(response.status_code)
# 响应的内容 ---> str 
print(response.text)
# 返回的字节串 -- bytes
print(response.content)
# 修改字符编码
response.encoding = 'utf-8'
print(response)
# 返回实际的url 
print(response.url)

# post请求


