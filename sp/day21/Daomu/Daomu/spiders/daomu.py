# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        # 标题和链接:
        title_list = response.xpath("//li[contains(@id,'menu-item-20')]/a")
        for each_title in title_list:
            item = DaomuItem()
            item['title'] = each_title.xpath('./text()').get()
            a_link = each_title.xpath('./@href').get()
            yield scrapy.Request(
                url = a_link,
                callback=self.parse_second_page,
                meta={'item':item}
            )

    def parse_second_page(self,response):
        item = response.meta['item']
        article_name = response.xpath('//article/a') 
        for each_name in article_name:
            name_link = each_name.xpath('./@href').get()
            name = each_name.xpath('./text()').get()
            yield scrapy.Request(
                url=name_link,
                callback=self.parse_third_page,
                meta={'item':item,'name':name}
            )

    def parse_third_page(self,response):
        item = response.meta['item']
        item['name'] = response.meta['name']
        content = response.xpath('//article[@class="article-content"]//p/text()').extract()
        item['content'] = '\n'.join(content)
        # {'title':'七星鲁王宫','name':'第二章','content':'fnsjadkfnkasjfk'}
        yield item

# 盗墓比较的 部
# 每部的章节 章节
#   每个章节的具体的内容