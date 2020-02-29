"""
    bilibili   滑动登陆代码
    2020-02-29 19:39
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import getpass

class BiliibiliSpider:
    def __init__(self,password):
        self.url = 'https://passport.bilibili.com/login'
        self.browser = webdriver.Chrome()
        # 显式等待
        self.wait = WebDriverWait(self.browser,100)
        # 用户名
        self.username = '18667018590'
        self.passwd = password

    def login(self):
        """
            打开浏览器填充密码和帐号
        """   
        self.browser.get(self.url)
        # 获取用户名输入框
        username_element = self.wait.until(EC.presence_of_element_located(
            (By.ID,'login-username'))
            ) 
        # 获取密码输入框 
        password_element = self.wait.until(EC.presence_of_element_located(
            (By.ID,'login-passwd'))
        )
        # 填充账户名和密码
        username_element.send_keys(self.username)
        password_element.send_keys(self.passwd)


    def main(self):
        self.login()

if __name__ == "__main__":
    import getpass
    password = getpass.getpass('PASSWORD:')
    b = BiliibiliSpider(password)
    b.main()