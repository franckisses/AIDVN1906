
import requests
from fake_useragent import UserAgent

url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/202002/20200200024708.shtml'

response = requests.get(url=url,headers={
    'User-Agent':UserAgent().random
})
print(response.status_code)
with open('test.html','w') as f:
    f.write(response.text)