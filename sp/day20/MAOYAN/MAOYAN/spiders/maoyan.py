# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']
    offset = 0 

    def parse(self, response):
        all_movie_elements = response.xpath('//dl[@class="board-wrapper"]/dd')
        print(all_movie_elements)
        for each_element in all_movie_elements:
            item = MaoyanItem()
            item['title'] = each_element.xpath('./a/@title').get().strip()
            item['actor'] = each_element.xpath('.//p[@class="star"]/text()').get().strip()
            item['release_time'] = each_element.xpath('.//p[@class="releasetime"]/text()').get().strip()
            yield item

        self.offset += 10
        if self.offset <= 90:
            url = 'https://maoyan.com/board/4?offset={}'.format(self.offset)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    
