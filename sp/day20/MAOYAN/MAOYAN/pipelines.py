# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class MaoyanPipeline(object):
    def process_item(self, item, spider):
        if item.get('title') == '泰坦尼克号':
            raise DropItem('我抛出了错误！')
        else:
            print("this is item:",item)
            print("this is spider:",spider)
            return item

# # item pipeline 将数据结构化 存储