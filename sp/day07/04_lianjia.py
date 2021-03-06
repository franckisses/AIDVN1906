""" 
    链家二手房爬虫
"""
import time
import random

import requests
from lxml import etree
from fake_useragent import UserAgent

# 调出xpath mac  command + shift + x
#               ctrl + shift  + x

class LianjiaSpier:
    def __init__(self):
        self.Base_url = 'https://bj.lianjia.com/ershoufang/pg{}/'
        self.headers = {'User-Agent':UserAgent().random }

    def parse_html(self,url):
        html = self.get_html(url)  
        text = etree.HTML(html)
        # 先匹配页面的所有的li 对象 一共是30个
        print('正在抓取的URL是：%s'%url)
        li_list = text.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        # 依次遍历每一个对象。获取该对象中的所有房源有效信息
        for index,each_li in enumerate(li_list):
            print('正在抓取第%d条'%index)
            item = {}
            # 房源的名字
            item['house_name'] = each_li.xpath('.//div[@class="title"]/a/text()')[0]
            # 房源的地址 先拿小区名 在拿地址
            # TODO 如果匹配出来的数据是空的，可以使用表达式进行替换。
            #         house_name if house_name else None
            address_1 = each_li.xpath('//div[@class="positionInfo"]/a[1]/text()')
            address_2 = each_li.xpath('//div[@class="positionInfo"]/a[2]/text()')
            item['address'] = address_2[0] + '-' + address_1[0]
            h_list = each_li.xpath('.//div[@class="houseInfo"]/text()')[0].split('|')
            if len(h_list) != 7:
                item['model'] = None
                item['area'] = None
                item['direct'] = None
                item['decorate'] = None
                item['floor'] = None
                item['year'] = None
                item['house_type'] = None
            else: 
                item['model'] = h_list[0]
                item['area'] = h_list[1]
                item['direct'] = h_list[2]
                item['decorate'] = h_list[3]
                item['floor'] = h_list[4]
                item['year'] = h_list[5]
                item['house_type'] = h_list[6]
            item['totalPrice'] = each_li.xpath('.//div[@class="totalPrice"]/span/text()')[0]
            item['unitPrice'] = each_li.xpath('.//div[@class="unitPrice"]/span/text()')[0]
            # TODO 依次一行的存储，因为在这就是一条一条的获取。
            print(item)
            
    def save_file(self,house_info):
        import csv 
        with open('lianjia_bj.csv','a') as f:
            writer = csv.writer(f)
            writer.writerow([1,2,3,4,5,6,7,8])
            # 多行存储
            writer.writerows([(),(),(),(),])

    def get_html(self,url):
        """
        向链家网发送请求。将返回的html转成字符串
        """
        try:
            html = requests.get(url=url,headers=self.headers,timeout=4.0).text
        except Exception as e:
            print('[Error]:',e)
        else:  
            return html

    def main(self):
        # 抓取北京市二手房信息
        # https://bj.lianjia.com/ershoufang/pg100/
        for i in range(1,3):
            url = self.Base_url.format(i)
            self.parse_html(url)
            time.sleep(random.randint(1,3))
            print('正在下载第%d页'%i)


if __name__ == "__main__":
    lianjia = LianjiaSpier()
    lianjia.main()