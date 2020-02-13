"""
   这是一个二手房之家的全站抓取脚本,数据解析方式主要是通过正则去匹配。

author : franck
email : franck_gxu@outlook.com
datetime : 2020-02-13 21:11
"""
from urllib import request
import re
import time
from hashlib import md5

from fake_useragent import UserAgent
from mysqlhelper import DatabaseHelper

class CarSpider:
    def __init__(self):
        self.Baseurl = 'https://www.che168.com/'
        self.headers = {
            'User-Agent': UserAgent().ie
        }
        self.db = DatabaseHelper(database='cardb')
        #mysql> create database cardb default charset utf8;

    def parse_html(self,url):
        """
        用来获取列表页的数据
        """
        list_html = self.get_html(url)
        # 拿到网页内容之后：做解析。
        html_list_reg ='<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>'
        href_list = self.regex_method(html_list_reg,list_html)
        for each_page in href_list:
            second_url = 'https://www.che168.com' + each_page
            # 1.通过对URL进行md5加密,指纹
            s = md5()
            s.update(second_url.encode())
            finder_type = s.hexdigest()
            # 此方法是用来检查指纹是否在数据库中存在 如果不存在返回 True反之False   # 布隆过滤器 
            if self.check_finger(finder_type):
                print('准备获取详情页数据')
                # TODO 如果获取详情页面数据失败，怎么处理处理url
                if self.get_detail(second_url):
                    sql = 'insert into finger values(%s)'
                    self.db.execute(sql,[finder_type])
                else:
                    # 获取详情页面数据失败的处理方式
                    print('[error]:','获取该页数据失败',second_url)
            else:
                continue   
            # 2.判断该指纹是否在mysql中，如果是那么跳过
            # 2.2 如果不存在，那么没爬过。获取数据，如果获取完之后，将该条指纹存入到mysql中。  
            # 3 将获取到的详情页数据全部存入到mysql中。  
            # 4 将全国所有的城市通过正则匹配出来
            # 如何判断数据已经爬取并且成功。将链接存入到mysql中。
        

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
        # TODO 对数据进行持久化存储，csv mysql 都行。
        print('this is detail car:',car_list)
        if car_list:
            return True
        return False

    def check_finger(self,finder_type):
        # 首先定义一个查询sql语句
        sql = 'select request_finger from finger where request_finger=%s'
        # 如果self.db.selct 返回的非None值，那么证明是有此指纹
        #                   返回的是None，那么此指纹还没有存入到mysql
        if self.db.select(sql,[finder_type]):
            return False
        return True

    def get_city(self):
        # 1.获取网站主页代码
        text = self.get_html(self.Baseurl)
        # 2.通过正则匹配出网站全国所有城市
        regex_pattern  = r'<a pidname=.*?href="(.*?)">(.*?)</a>'
        all_city_list = self.regex_method(regex_pattern,text)
        print(all_city_list)
        # 3.再依次抓取抓取全国城市中的二手车信息


    # 程序入口主函数
    def run(self):
        self.get_city()

    
if __name__ == "__main__":
    spider = CarSpider()
    spider.run()

# # 思路：
# 1. 首先通过域名去访问该网站，拿到所有城市二级链接。
# 2. 此时二级城市链接就是列表页。
# 3. 再根据列表页抓取详情页数据。


# https://www.che168.com/china/a0_0msdgscncgpi1lto8csp1ex/#pvareaid=104649
