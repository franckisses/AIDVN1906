
from selenium import webdriver

import time

# 创建谷歌浏览器驱动对象
browser = webdriver.Chrome()

# 访问页面
browser.get('http://www.baidu.com')
# 访问其他页面
time.sleep(5)
browser.get('https://www.jianshu.com')
# 等待
time.sleep(100)

# 退出自动化控制程序
browser.quit()






