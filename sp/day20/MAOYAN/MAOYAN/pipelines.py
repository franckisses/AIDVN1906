# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

# class MaoyanPipeline(object):
#     def process_item(self, item, spider):
#         if item.get('title') == '泰坦尼克号':
#             raise DropItem('我抛出了错误！')
#         else:
#             print("this is item:",item)
#             print("this is spider:",spider)
#             return item

# # item pipeline 将数据结构化 存储
import pymysql
import time 
from scrapy.mail import MailSender
# # 数据持久化 Mysql
class MaoYanMysqlPipeline(object):
    
    def open_spider(self,spider):
        print('爬虫开始工作了.....')
        mailer = MailSender(smtphost='smtp.qq.com',smtpuser='572708691@qq.com',smtppass='bshyjfuxberdbbjg',mailfrom='DADASHOP<572708691@qq.com>')
        # mailer = MailSender.from_settings()
        test = mailer.send(to=["842549758@qq.com"], subject="Some subject", body="Some body")
        print('test---',test)
        self.start = time.time()

        self.db = pymysql.connect(
            host='localhost',
            user='root',
            port=3306, # port 必须是数字
            password='123456',
            database='maoyan_film',
            charset='utf8'
        )
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        # {'actor': '主演：罗伯托·贝尼尼,尼可莱塔·布拉斯基,乔治·坎塔里尼',
        # 'release_time': '上映时间：2020-01-03',
        # 'title': '美丽人生'}
        sql = 'insert into board values(%s,%s,%s);'
        data = [
            item['actor'][3:],
            item['title'],
            item['release_time'][5:]
        ]
        self.cursor.execute(sql,data)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
        print('爬虫运行的时间是:',time.time()-self.start)

        
# scrapy crawl maoyan -o maoyan.json
# scrapy crawl maoyan -o maoyan.csv
# scrapy crawl maoyan -o maoyan.xml
# scrapy crawl maoyan -o maoyan.pickle   # pickle 
# scrapy crawl maoyan -o ftp://user:password@code.tarena.com.cn/maoyan.csv

