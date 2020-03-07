# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://baidu.com']

    def parse(self, response):
        
        print('-'*30)
        print(response.xpath('//title/text()')).get()
        print('-'*30)
        
        # 9:05 回来

# 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
#  'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
#  'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
#  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
#  'middle.middlewares.MiddleDownloaderMiddleware',
#  'scrapy.downloadermiddlewares.retry.RetryMiddleware',
#  'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
#  'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
#  'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
#  'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
#  'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
#  'scrapy.downloadermiddlewares.stats.DownloaderStats']