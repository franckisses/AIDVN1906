


import requests

# requests.get() # url headers
# 添加查询字符串
# params 
# urlencode()
# urlparse()
# http://tieba.baidu.com/f/good?kw=%CE%E4%BA%BA&cid=1&fr=ala0&tpl=5

# http://tieba.baidu.com/f?ie=utf-8&kw=%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4&fr=search
# http://tieba.baidu.com/f?ie=utf-8&kw=%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4&fr=search&red_tag=f1697429271
keyword = str(input('请输入要查询的吧名：'))
params = {
    'ie':'utf-8',
    'kw':keyword,
    'fr':'search'
}
response = requests.get(
    url='http://tieba.baidu.com/f?',
    params= params,
    headers = {
        'User-Agent':'Mozilla/5.0'
        }
    )
print(response.url)
# print(response.text)


