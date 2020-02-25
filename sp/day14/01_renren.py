

import requests
from lxml import etree


url = 'http://www.renren.com/576865529/profile'


response = requests.get(
    url=url,
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
        # 'Cookie': 'JSESSIONID=abcWNaPkQdHD9_RJlM8bx; anonymid=k71y67xx8v8suj; depovince=BJ; jebecookies=9ccd74d0-ff77-44b3-b484-4da9bec6bc07|||||; _r01_=1; ick_login=3a7e1d07-1e58-4c58-b835-55ce0b1fcd06; taihe_bi_sdk_uid=fe480d4ce0bf2c5464e9ffcd622cb065; taihe_bi_sdk_session=a666ed81ed629a4e02367475adbb71f2; _de=6B871D83B462D7B68E49A581F847F522; p=478c0b2ae76160a9328e5435b166650b9; first_login_flag=1; ln_uact=18667018590; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=36e3f0f2b955011ca355fc5f1b6bb41d9; societyguester=36e3f0f2b955011ca355fc5f1b6bb41d9; id=576865529; xnsid=8362f9b3; loginfrom=syshome; wp_fold=0'
    }
)

text = response.text

html = etree.HTML(text)
colleage = html.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()') 
print(colleage)










