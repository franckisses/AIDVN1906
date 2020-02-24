"""
    小米应用商店爬虫
"""
import requests
import time
from queue import Queue
from fake_useragent import UserAgent
import json
import csv
from lxml import etree


class XiaomiSpider:
    def __init__(self):
        # 第一页 用来获取所有应用类别
        self.category_url = 'http://app.mi.com/category/15'
        # 获取纯数据的URL
        self.data_url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'
        self.headers = {
            'User-Agent':UserAgent().random
        }
        self.queue = Queue()

    # 获取网页的类型和类型码
    def get_type_code(self):
        pass

    # 获取app的总页数
    def get_total_page(self):
        pass

    # 解析页面
    def parse_html(self):
        pass

    # 主函数启动项目
    def main(self):
        """
            思路：
            1。我们可以生成很多个URL。
                将URL放入到队列中。
            2.通过threading模块来创建多个线程
                线程发送请求。解析页面。将数据存入到csv中。

        """
        # TODO 1. 生成所有的URL放入的队列中
        #      2. 创建线程去解析网页，并且将数据存入到csv中

if __name__ == "__main__":
    xm = XiaomiSpider()
    xm.main()
