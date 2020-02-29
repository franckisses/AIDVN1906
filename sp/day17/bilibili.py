"""
    bilibili   滑动登陆代码
    2020-02-29 19:39
"""
import time
import getpass
import base64

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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
        time.sleep(3)
        # 构建获取图片的js代码
        getImages = "return document.getElementsByClassName('"+canvas_class+"')[0].toDataURL('image/png');"
        images_data = self.browser.execute_script(getImages)
        # 截取图片内容
        image = images_data[images_data.find(',')+1:]
        # 对图片内容进行解码
        image_binary = base64.b64decode(image)
        # 存储图片
        try:
            with open(filename,'wb') as f:
               f.write(image_binary)
            return True
        except:
            return False
        

    def main(self):
        # 登陆触发检测
        self.login()
        # 获取有缺口的图片
        if not self.save_bg('bg.png','geetest_canvas_bg geetest_absolute'):
            print('保存有缺口的图片上失败!')
        if not self.save_bg('fullbg.png','geetest_canvas_fullbg geetest_fade geetest_absolute'):
            print('保存完整图片失败！')

if __name__ == "__main__":
    import getpass
    password = getpass.getpass('PASSWORD:')
    b = BiliibiliSpider(password)
    b.main()