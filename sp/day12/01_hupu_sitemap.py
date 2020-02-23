"""
    虎扑 sitemap 示例
"""

import requests
import re
import time

from fake_useragent import UserAgent



class HupuJrsSpider:
    def __init__(self):
        self.sitemap_url = 'https://nba.hupu.com/players/index.xml'
        self.headers = {
            'User-Agent': UserAgent().random
        }
    def get_html(self,current_url):
        """获取网站页面"""
        try:
            response = requests.get(
                url=current_url,
                headers = self.headers   
            )
        except Exception as e:
            print('[%s]'%response.status_code,e)
        return response.text

    def regex_method(self,html):
        pattern = re.compile(r'<loc>(.*?)</loc>',re.S)
        result = pattern.findall(html)
        return result
    
    def parse_one_html(self,current_url):
        html = self.get_html(current_url)
        result = self.regex_method(html)
        self.parse_two_html(result)

    def parse_two_html(self,url_list):
        for i in url_list:
            html = self.get_html(i)
            single_page_player = self.regex_method(html)
            self.get_each_player(single_page_player[0])
            break


    def get_each_player(self,current_url):
        html = self.get_html(current_url)
        # TODO 通过xpath去匹配所有球员的信息



        
    def main(self):
        self.parse_one_html(self.sitemap_url)
        


if __name__ == "__main__":
    hp = HupuJrsSpider()
    hp.main()


