# -*- coding: utf-8 -*-

# Scrapy settings for MAOYAN project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MAOYAN'

SPIDER_MODULES = ['MAOYAN.spiders']
NEWSPIDER_MODULE = 'MAOYAN.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MAOYAN (+http://www.yourdomain.com)'

# Obey robots.txt rules

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
  # 'Cookie':'__mta=146102795.1582805409453.1583416792975.1583416798673.36; uuid_n_v=v1; uuid=17D894E0595A11EAAB15BF1175455FAC988932E2E05D46B5A548E36A512324E2; _lxsdk_cuid=170868ddd51c8-03003f573d71ae-39697407-1fa400-170868ddd52c8; _lxsdk=17D894E0595A11EAAB15BF1175455FAC988932E2E05D46B5A548E36A512324E2; mojo-uuid=8f9f7a91b7f41d43494fdb0c14b7f5f2; _csrf=889bef00926fe74f34b29f5af571e30a4a9685b78ba6dfcd75727a2a09fcd6a1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1582805409,1583396209; __mta=146102795.1582805409453.1583410507705.1583410519181.20; mojo-session-id={"id":"df2a4696d103547d1b2208beb8dd61d4","time":1583415993441}; mojo-trace-id=11; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1583416798; _lxsdk_s=170aaf2a465-ddf-45f-1e5%7C%7C15',
  # 'Host':'maoyan.com',
  # 'Pragma': 'no-cache',
  # 'Sec-Fetch-Dest': 'document',
  # 'Sec-Fetch-Mode': 'navigate',
  # 'Sec-Fetch-Site': 'none',
  # 'Sec-Fetch-User': '?1',
  # 'Upgrade-Insecure-Requests': '1',
  # 'Cache-Control': 'no-cache',
  # 'Referer':'https://maoyan.com/board'

}
LOG_LEVEL = 'WARNING'
LOG_FILE = 'maoyan.log'

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'MAOYAN.middlewares.MaoyanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'MAOYAN.middlewares.MaoyanDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'MAOYAN.pipelines.MaoyanPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
