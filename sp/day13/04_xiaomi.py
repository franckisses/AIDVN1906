"""
    小米应用商店爬虫
"""
import requests
import time
import math
from queue import Queue
from fake_useragent import UserAgent
import json
import csv
from lxml import etree
from threading import Thread
from threading import Lock

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
        self.lock = Lock()

    # 获取网页的类型和类型码
    def get_type_code(self):
        """获取所有的类型应用的id"""
        try:
            response = requests.get(
                url=self.category_url,
                headers = self.headers
            )
        except Exception as e:
            print('[Error]-获取网页应用ID失败原因是：',e)
        else:
            text =response.text
        html = etree.HTML(text)
        # 找到所有应用的标签
        print('-----')
        li_list = html.xpath('//ul[@class="category-list"]/li/a')
        # 遍历所有分类应用
        for each_a in li_list:
            app_type = each_a.xpath('./text()')[0]
            # 当前应用分类的id
            type_id = each_a.xpath('./@href')[0].split('/')[-1]
            each_app_total = self.get_total_page(type_id)
            # 当前应用分类的页码数
            each_app_page  = math.ceil(each_app_total / 30) 
            self.put_url_in_queue(type_id,each_app_page)
            print('正在将%s的链接放入到队列中...'%app_type)
            time.sleep(2)
    # 获取app的总页数
    def get_total_page(self,type_id):
        url = self.data_url.format(0,type_id)
        try:
            response = requests.get(
                url=url,
                headers = self.headers
            )
        except Exception as e:
            print('[Error]-获取网页应用ID失败原因是：',e)
        else:
            return response.json()['count']
        

    def put_url_in_queue(self, type_id,each_app_page):
        for i in range(0,each_app_page):
            url = self.data_url.format(i,type_id)
            self.queue.put(url)

    def parse_html(self):
        # 此函数的功能是用来做请求-解析-数据的存储
        while True:
            if not self.queue.empty():
                url = self.queue.get()
                try:
                    response = requests.get(
                        url = url,
                        headers = self.headers
                    ).json()
                except Exception as e:
                    print('[Error]:',e,'\n',response)
                for app in response['data']:
                    # writerows([(),(),()])
                    self.lock.acquire()
                    with open("xiaomi1.json","a",encoding="utf-8") as f:
                        f.write(json.dumps(app,ensure_ascii=False)+"\n")
                    self.lock.release()
                    time.sleep(2)
                    # 将小米应用商店的数据存入到json
                # {"appId":108048,"displayName":"王者荣耀","icon":"http://file.market.xiaomi.com/thumbnail/PNG/l62/AppStore/0eb7aa415046f4cb838cfe5b5d402a5efc34fbb25","level1CategoryName":"网游RPG","packageName":"com.tencent.tmgp.sgame"}
            else:
                break

    # 主函数启动项目
    def main(self):
        """
            思路：
            1.我们可以生成很多个URL。
                将URL放入到队列中。
            2.通过threading模块来创建多个线程
                线程发送请求。解析页面。将数据存入到csv中。
        """
        # 1. 获取所有的应用分类的id
        self.get_type_code()
        #      2. 创建线程去解析网页，并且将数据存入到csv中
        t_list =[]
        for i in range(4):
            t = Thread(target=self.parse_html)
            t_list.append(t)
            t.start()
        
        for i in t_list:
            t.join()


if __name__ == "__main__":
    xm = XiaomiSpider()
    xm.main()


# 今日内容：
    # 小米应用商店
    # 人人网 cookie
    # selenium 

# http://app.mi.com/categotyAllListApi?page=1&categoryId=15&pageSize=30

# http://app.mi.com/details?id=jp.usaya.tofu.bnn
#                         "jp.usaya.tofu.bnn"     


# http://app.mi.com/categotyAllListApi?page=0&categoryId=19&pageSize=30

# 生成所有应用的数据接口
#     已经知道 应用页数
#             应用的分类ID
# {"appId":108048,
# "displayName":"王者荣耀",
# "level1CategoryName":"网游RPG",
# "packageName":"com.tencent.tmgp.sgame"
# }



