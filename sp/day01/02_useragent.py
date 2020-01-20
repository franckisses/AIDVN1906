
from urllib import request

res = request.urlopen('http://httpbin.org/get')
print(res.read().decode())