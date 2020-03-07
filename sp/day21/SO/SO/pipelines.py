# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from urllib.request import urlretrieve

class SoPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url = item['img_url'],
            meta = {'title':item['title']} 
        )
    
    def file_path(self, request, response=None, info=None):
        name = request.meta['title']
        media_ext = os.path.splitext(request.url)[1]
        return 'images/%s%s' % (name, media_ext)

# 存储地址 settings.py中
# IMAGES_STORE = '/Users/gongyan/Desktop/AIDVN1906/sp/'