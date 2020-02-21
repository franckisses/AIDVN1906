
from lxml import etree
from fake_useragent import UserAgent
import requests
import re


class GovSpider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.second_url = None
        self.third_url = None
        self.Base_url = 'http://www.mca.gov.cn'

    def parse_html(self):
        html = self.get_html(self.url)
        text = etree.HTML(html)
        self.second_url = self.Base_url + text.xpath(
            '//table[@class="article"]//tr[2]/td[2]/a/@href'
            )[0]
        print('二级链接为:',self.second_url)
        print('此时通过二级链接请求重定向页面：')
        second_html = self.get_html(self.second_url)
        # 

        reg_exp = 'window.location.href="(.*?)"'
        self.third_url = self.regex_method(reg_exp,second_html)
        print('三级页面的链接：',self.third_url)
        third_html = self.get_html(self.third_url)
        self.get_code(third_html)

    def regex_method(self,reg_exp,html_str):
        pattern = re.compile(reg_exp, re.S)
        result = pattern.findall(html_str)[0]
        return result
    
    def get_code(self,html_str):
        """
        TODO
        匹配网页内容：
          code:      //tr[@height=19]/td[2]/text()
          district:  //tr[#height=19]/td[3]/text()
        """
    def get_html(self,current_url):
        # TODO try
        response = requests.get(url=current_url,headers={
                'User-Agent': UserAgent().random
            })
        if response.status_code == 200:
            return response.text

    def main(self):
        self.parse_html()

if __name__ == "__main__":
    go = GovSpider()
    go.main()


# //table[@class="article"]/tbody/tr[2]/td[2]/a/@href