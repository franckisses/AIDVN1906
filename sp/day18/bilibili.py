"""
    bilibili   滑动登陆代码
    2020-02-29 19:39
"""
import time
import getpass
import base64
import random

import PIL.Image as image
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


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
        time.sleep(2)
        # 构建获取图片的js代码
        getImages = "return document.getElementsByClassName('"+canvas_class+"')[0].toDataURL('image/png');"
        images_data = self.browser.execute_script(getImages)
        # 截取图片内容
        time.sleep(1)
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
        left = 43
        # 获取图片的长度和宽度的每个像素点的位置
        
        for i in range(left,bg.size[0]):
            for j in range(bg.size[1]):
                if not self.is_pixel_match(bg,full_bg,i,j):
                    left = i
                    return left
        return left

    def is_pixel_match(self,bg,full_bg,x,y):
        """
            判断两个像素点是否匹配
            img1 有缺口的图片读取对象
            img2 没有缺口的图片读取对象
            x 相当于横坐标
            y 相当于纵坐标
        """
        pix1 = bg.load()[x,y]
        pix2 = full_bg.load()[x,y]
        color_args = 60
        #  每个点的像素的差值的绝对值，如果都小于阈值的话那么我们认为不是缺口处
        #  两个像素的绝对值差值小于阈值
        if  (abs(pix1[0] - pix2[0]) < color_args) and (abs(pix1[1] - pix2[1]) < color_args) and (abs(
                pix1[2] - pix2[2]) < color_args):
            return True
        else:
            return False

    def get_trace(self,distance):
        """
            获取滑块移动的轨迹
            distance :像素的偏移量
        """
        # 存储移动的轨迹的路径
        trace_back = []
        # 存储当前移动的总距离
        curent = 0
        middle = distance * 4 / 5 # 中间值
        if distance > 110:
            t = 0.21
        else:
            t = 0.15 # 每次加速移动或者减速移动的时间
        v = 0 # 刚开始移动的时候初速度为0 
        while curent < distance:
            if curent < middle:
                # 做加速运动
                a = 2
            else:
                a = -3
            v0 = v # v0 每单位时间开始做移动的初速度
            v = v0 + a * t# 当前的速度
            move_tem = v*t + 1/2*a*t*t # 在单位时间内的移动距离
            curent += move_tem # 计算当前的位移
            trace_back.append([round(move_tem),random.choice([1,-1,0,0,0,0])])
        return trace_back

    def move_button(self,element,trace):
        """
            移动滑块
        """
        start_time = time.time()
        ActionChains(self.browser).click_and_hold(element).perform()
        trace = trace[::-1]
        for each_trace in trace:
            x,y = each_trace
            ActionChains(self.browser).move_by_offset(
                xoffset = x,
                yoffset = y
            ).perform()
        ActionChains(self.browser).release().perform()
        print('滑动滑块时间为：',time.time()-start_time)

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
        print('---当前的偏移量是：%d--'%distance)
        # 初速度为0的匀速加速运动
        # 初速度不为0的匀减速/匀减速运行
        trace = self.get_trace(distance - 9)
        print(trace)
        # 获取滑块：
        try:
            element = self.browser.find_element_by_class_name(
                'geetest_slider_button'
                )
        except Exception as e:
            print('获取滑块失败')
        # 将滑块移动到缺口处
        self.move_button(element,trace)
        

if __name__ == "__main__":
    import getpass
    password = getpass.getpass('PASSWORD:')
    b = BiliibiliSpider(password)
    b.main()


# Pillow                             5.4.1

# 加速运动 初速度为v0 = 0 
#                 a 加速度
#                 t 时间
# s = 1/2*a*t^2
# v = a*t 

# 减速运动
# 减速运动的初速度：v = V0 + at
# s = v* t + 1/2 * a*t ^2 


# [[0, -2], [0, -1], [0, -2], [0, 1], [0, 2], [0, -2], [0, 2], [0, -1], [0, -2], [0, 2],
#  [1, 1], [1, 1], [1, 2], [1, 1], [1, -2], [1, 2], [1, 2], [1, 1], 
#  [1, -1], [1, 1], [1, -2], [1, -1], [1, 1], [1, -1], [1, -2], [1, -1],
#   [1, 1], [1, -1], [1, -2], [1, 2], [1, -1], [1, -1], [2, 2], [2, -2], 
#   [2, 2], [2, -2], [2, 2], [2, 1], [2, -2], [2, -1], [2, 2], [2, 2], 
#   [2, -2], [2, -2], [2, 1], [2, 2], [2, 2], [2, 2], [2, 2], [2, -2],
#    [2, -1], [2, 2], [2, -1], [2, -2], [2, 1], [3, 1], [3, -2], [3, 1],
#     [3, -2], [3, -1], [3, 1], [3, 1], [3, -1], [3, 2], [3, 2], [3, 2], 
#     [3, -2], [3, -1], [3, 1], [3, -1], [3, 2], [3, 2], [3, -1], [3, -1],
#      [3, -1], [3, 1], [3, 2], [4, -1], [4, 2], [4, -2], [4, 2], [4, 2], 
#      [3, -1], [3, 2], [3, 1], [3, -2], [3, -1], [3, 1], [3, 2], [3, 1]]

# scripts
# python.exe
# teamview

