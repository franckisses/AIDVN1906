# -*- coding: utf-8 -*-
import scrapy
import json


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
            img['title']
            img['qhimg_downurl']
        # 中间件