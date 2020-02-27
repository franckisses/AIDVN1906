"""
    选项卡的管理
"""

from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.execute_script('window.open()')
# 选项卡管理工具
print('当前的选项卡有如下：')
print(browser.window_handles)
# ['CDwindow-0412EFE4A0B94C8260803973AE513F00', 
# 'CDwindow-6F52A63ADF82A64FC7FD52B26C07F9D3']
# 切换到第二个选项卡中
browser.switch_to_window(browser.window_handles[1])
browser.get('https://jianshu.com')
time.sleep(5)
# 如果有多个选项卡的时候
# browser.close()                      只会关闭当前的选项卡
# browser.quit()                       关闭所有的选项卡
browser.quit()
browser.close() 
# print(browser.window_handles)                           # 9:03 