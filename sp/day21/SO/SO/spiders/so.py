# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SoItem

class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    url = 'https://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'


    def start_requests(self):
        for n in range(0,301,30):
            url = self.url.format(n)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    def parse(self, response):
        data = json.loads(response.text)
        for img in data['list']:
            item = SoItem()
            item['title'] = img['title'] 
            item['img_url'] = img['qhimg_url']
            yield item