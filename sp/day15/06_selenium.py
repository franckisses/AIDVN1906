"""
    腾讯招聘截图
"""

from selenium import webdriver
import time

browser = webdriver.Chrome()


browser.get('https://careers.tencent.com/search.html')
# time.sleep(5)
browser.save_screenshot('/Users/gongyan/Desktop/AIDVN1906/sp/day15/tencent1.png')
# browser.quit()
