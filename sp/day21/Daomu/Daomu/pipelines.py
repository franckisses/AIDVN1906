# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os

class DaomuPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        content = item['content']
        name = item['name']
        FILE_PATH = '/Users/gongyan/Desktop/AIDVN1906/sp/{}/'.format(title)
        # /Users/gongyan/Desktop/AIDVN1906/sp/盗墓笔记1：七星鲁王宫/七星鲁王 第一章 血尸.txt
        if not os.path.exists(FILE_PATH):
            os.makedirs(FILE_PATH)

        filename = FILE_PATH + name + '.txt'
        with open(filename,'w') as f:
            f.write(content)

        return item
