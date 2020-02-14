

from urllib import request
from fake_useragent import UserAgent
import re

res = request.Request('https://www.che168.com/dealer/345215/36240665.html?pvareaid=100519&userpid=340000&usercid=340100#pos=2#page=1#rtype=10#isrecom=0#filter=0aa0_0a0_0a0_0#module=10#refreshid=0#recomid=0#queryid=#cartype=70',
    headers={'User-Agent':UserAgent().ie})
try:
    response = request.urlopen(res)
except Exception as e:
    print(e)
html = response.read().decode('gb2312','ignore')

pattern = re.compile(r'<a action="usc_2sc_detail_photo_show".*?>\
    <img.*?data-original="(.*?)".*?></a>',re.S)
result = pattern.findall(html)
print(result)