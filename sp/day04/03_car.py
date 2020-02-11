# 网站的链接：https://www.che168.com/beijing/a0_0msdgscncgpi1lto8csp1exx0/

from urllib import request
import re
import time

from fake_useragent import UserAgent
from mysqlhelper import DatabaseHelper

class CarSpider:
    def __init__(self):
        # 初始化的url
        self.url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1lto8csp{}exx0/'
        # 构造一个请求头
        self.headers = {
            'User-Agent':UserAgent().ie
        }
        # 初始化数据库链接
        self.db = DatabaseHelper(database='cardb')
        #mysql> create database cardb default charset utf8;

        # 思考：
        # 1.如何去判断我们的链接 那个是已经抓取过了。[如何去重]
        # 2.如何做深度爬取获取第二页数据
        # 3.如何保存图片？ open方法,
    def parse_html(self,url):
        """
        用来获取列表页的数据
        """
        list_html = self.get_html(url)
        # 拿到网页内容之后：做解析。
        html_list_reg ='<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>'
        href_list = self.regex_method(html_list_reg,list_html)
        
        print('--------------')
        for each_page in href_list:
            second_url = 'https://www.che168.com' + each_page

            # 如何判断数据已经爬取并且成功
            # 爬取第二页的数据
            print('准备获取详情页数据')
            self.get_detail(second_url)
            break
        
    

    # 用来发送请求
    def get_html(self,current_url):
        """向当前出入的URL发送请求，获取页面数据
            返回值为html （str）
        """
        req = request.Request(url=current_url,headers=self.headers)
        try:
            res = request.urlopen(req)
            html = res.read().decode('gb2312','ignore')
            return html
        except Exception as e:
            print('[Error]:',e)
        

    def regex_method(self,reg,html):
        pattern = re.compile(reg,re.S)
        url_list = pattern.findall(html)
        return url_list


    # 获取第二页数据
    def get_detail(self,current_url):
        print('正在开始抓取此链接：',current_url)
        detail_html = self.get_html(current_url)
        detail_reg = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<ul class="brand-unit-item fn-clear">.*?<li>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<h4>(.*?)</h4>.*?<span class="price" id="overlayPrice">￥(.*?)<b'
        car_list =self.regex_method(detail_reg,detail_html)
        print('this is detail car:',car_list)

    # 程序入口主函数
    def run(self):
        for i in range(1,3):
            url = self.url.format(i)
            self.parse_html(url)
            break

    
if __name__ == "__main__":
    spider = CarSpider()
    spider.run()

