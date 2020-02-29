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
        # 找到点击登陆按钮
        button_login = self.browser.find_element_by_xpath(
            '//*[@id="geetest-wrap"]/div/div[5]/a[1]'
        )
        try:
            button_login.click()
        except Exception as e:
            print('[Error]:',e)

    def save_bg(self,filename,canvas_class):
        """
            保存图片
            1.图片名字，
            2.节点的名字
        """
        # full_image = ''
        time.sleep(3)
        getImages = "return document.getElementsByClassName('"+canvas_class+"')[0].toDataURL('image/png');"
        print(getImages)
        images_data = self.browser.execute_script(getImages)
        
        print(images_data[:20])

    def main(self):
        # 登陆触发检测
        self.login()
        # 获取完整图片 以及有缺口的图片
        self.save_bg('bg.png','geetest_canvas_bg geetest_absolute')


if __name__ == "__main__":
    import getpass
    password = getpass.getpass('PASSWORD:')
    b = BiliibiliSpider(password)
    b.main()