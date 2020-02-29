"""
    bilibili   滑动登陆代码
    2020-02-29 19:39
"""
import time
import getpass
import base64

import PIL.Image as image
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
        
    def get_length(self,img1,img2):
        """
            获取缺口的像素位置
            img1 有缺口的图片名
            img2 没有缺口的图片名
        """
        bg = image.open(img1)
        full_bg = image.open(img2)
        left = 50 
        # 获取图片的长度和宽度的每个像素点的位置
        for i in range(left,bg.size[0]):
            for j in range(bg.size[1]):
                if not self.is_pixel_match(bg,full_bg,i,j):
                    left = i
                    return left
                else:
                    continue
        return left

    def is_pixel_match(bg,full_bg,x,y):
        """
            判断两个像素点是否匹配
            img1 有缺口的图片读取对象
            img2 没有缺口的图片读取对象
            x 相当于横坐标
            y 相当于纵坐标
        """
        pix1 = bg.load()[x,y]
        # (149, 207, 238, 255)
        pix2 = full_bg.load()[x,y]
        # (149, 207, 238, 255)
        color_args = 60
        if (abs(pix1[0]-pix2[0] < color_args) and 
            abs(pix1[1]-pix2[1] < color_args) and 
            abs(pix1[2]-pix2[2] < color_args)):
            return True
        else
            return False



    def main(self):
        # 登陆触发检测
        self.login()
        # 获取有缺口的图片
        if not self.save_bg('bg.png','geetest_canvas_bg geetest_absolute'):
            print('保存有缺口的图片上失败!')
        if not self.save_bg('fullbg.png','geetest_canvas_fullbg geetest_fade geetest_absolute'):
            print('保存完整图片失败！')
        
        # 获取图片的缺口位置
        distance = self.get_length('bg.png','fullbg.png')
        # 初速度为0的匀速加速运动
        # 初速度不为0的匀减速/匀减速运行


if __name__ == "__main__":
    import getpass
    password = getpass.getpass('PASSWORD:')
    b = BiliibiliSpider(password)
    b.main()


# Pillow                             5.4.1