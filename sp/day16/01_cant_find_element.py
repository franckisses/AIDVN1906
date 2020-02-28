"""
    异常处理：  
        不能找到节点
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,

# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com')
# try:
#     browser.find_element_by_id('gongyan')
# except NoSuchElementException as e:
#     print('没找到这个节点')


# TimeoutException 因为网络或者协议的异常可以通过timeoutexception来捕获
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
# browser.find_element_by_id('gongyan')

#   
def function_test():
    try:
        response = requests.get(url).text
        return response
    except Exception as e:
        return False

