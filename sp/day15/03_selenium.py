
from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('https://maoyan.com/')
time.sleep(1)
browser.get('http://www.baidu.com/')
time.sleep(1)
browser.get('https://www.jianshu.com/')
# 回退
time.sleep(5)
browser.back()
print('向前')
browser.forward()
time.sleep(5)
# browser.back()
# time.sleep(5)

# 前进是forward()
browser.quit()



