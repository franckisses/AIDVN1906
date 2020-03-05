# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    actor = scrapy.Field()
    title = scrapy.Field()
    release_time = scrapy.Field() 
    # pass

# 验证爬取数据，检查字段
# 丢弃重复的数据











# engine:引擎： 处理所有的请求，以及数据流，触发事务，框架的核心
# item : 项目： 定义了爬取的数据结构，爬取的数据将会被赋值给Item对象
# spider: 爬虫程序（蜘蛛）：定义了网页爬取的起始url，以及解析网页响应对象的内容。
# schedule: 调度器： 接受引擎发过来的请求加入到队列中。
#     最后再从队列中拿出最先的请求对象给引擎。
# download:下载器: 主要发送请求，将网页内容返回给引擎。
# download middleware: 再引擎和下载器中间。可以处理请求和下载的参数。或者添加代理等
# spider middleware : 蜘蛛中间件： 主要处理数据流和新的请求
# pipelines: 负责将item中的内容做清洗以及数据存储。