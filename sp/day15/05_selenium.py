"""
    腾讯招聘源码
"""

from selenium import webdriver
import time

browser = webdriver.Chrome()


browser.get('https://careers.tencent.com/search.html')
time.sleep(5)

# page_sourse 属性  当前选项卡中网页加载完成之后的源代码

with open('tencent.html','a') as f:
    f.write(browser.page_source)