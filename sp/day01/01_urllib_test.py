
from urllib.request import urlopen
# 返回值是网站的相应对象
# res = urlopen('http://www.baidu.com')
# 获取相应内容的话 :
# read 返回的字节串
# text = res.read().decode()
# print(text)
#　返回实际资源url 地址 # 3xx
# print(res.geturl())
# 返回状态吗　
# print(res.getcode())

# 练习　使用此种方式请求必应
# https://cn.bing.com/
res = urlopen('https://cn.bing.com')
print(res.read().decode())

