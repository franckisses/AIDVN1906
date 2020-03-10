# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        # print(response.status_code)
        # url 
        print( '响应的url',response.url)
        # 响应码
        print('rest')
        print('响应码:',response.status)
        # 响应头
        print('响应头：',response.headers.getlist('Set-Cookie'))
        # url ---> http://host/article/19    /article/19
        print(response.urljoin('/article/19'))
        print('标题：',response.css('title'))
        
