
from urllib.request import urlopen

# 返回值是网站的相应对象
res = urlopen('http://www.baidu.com')


# 获取相应内容的话 :
# read 返回的字节串
text = res.read().decode()

print(text)
