# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 图片的名称
    title = scrapy.Field()
    # 图片的下载链接
    img_url = scrapy.Field()