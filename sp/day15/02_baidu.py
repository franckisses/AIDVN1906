


from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get('http://www.baidu.com')

# 找到输入框节点
input_element = browser.find_element_by_xpath('//*[@name="wd"]')
print(input_element)

print(browser.execute_script("return document.title")) # ctrl + 鼠标左键
# 往输入框中填写内容
input_element.send_keys('i find u!')
time.sleep(5)

browser.quit()




