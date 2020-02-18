
import requests
# proxies
# proxies = {
#     'http':'scheme://host:port',
#     'https':'scheme://host:prot'
# }
# response = requests.get(url=url,headers=headers,proxies=proxies)


response = requests.get(
        url='http://httpbin.org/get',
        proxies={
            'http':'http://80.232.126.94:80',
            'https':'https://80.232.126.94:80'
            },
        timeout=4
        )
print(response.text)

"""
{
  "args": {}, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
    "Accept-Encoding": "gzip", 
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6", 
    "Cache-Control": "max-age=0", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)", 
    "X-Amzn-Trace-Id": "Root=1-5e4bdb13-5a85522c2c0fc26460312a37"
  }, 
  "origin": "80.232.126.94", 
  "url": "http://httpbin.org/get"
}

"""

# 高匿名代理： 
#   通过设置了代理之后访问服务器，服务器端不能看到你真是的IP只能看到代理IP
# 普通代理：
#   服务端知道有代理IP访问，但是不知道客户端的具体IP。
# 透明代理  
#   服务端能看到真是IP也可以看到你的代理IP

