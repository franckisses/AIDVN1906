# -*-coding:utf-8 -*-

import random
import re
import time
import getpass

# 图片转换
import base64
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

import PIL.Image as image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def save_base64img(data_str, save_name):
    """
    将 base64 数据转化为图片保存到指定位置
    :param data_str: base64 数据，不包含类型
    :param save_name: 保存的全路径
    """
    img_data = base64.b64decode(data_str)
    file = open(save_name, 'wb')
    file.write(img_data)
    file.close()


def get_base64_by_canvas(driver, class_name, contain_type):
    """
    将 canvas 标签内容转换为 base64 数据
    :param driver: webdriver 对象
    :param class_name: canvas 标签的类名
    :param contain_type: 返回的数据是否包含类型
    :return: base64 数据
    """
    # 防止图片未加载完就下载一张空图
    bg_img = ''
    while len(bg_img) < 5000:
        getImgJS = 'return document.getElementsByClassName("' + class_name + '")[0].toDataURL("image/png");'
        bg_img = driver.execute_script(getImgJS)
        time.sleep(0.5)
    # print("bg_img: ", bg_img)
    if contain_type:
        return bg_img
    else:
        return bg_img[bg_img.find(',') + 1:]

# geetest_canvas_bg geetest_absolute
def save_bg(driver, bg_path="bg.png", bg_class="geetest_canvas_bg geetest_absolute"):
    """
    保存包含缺口的背景图
    :param driver: webdriver 对象
    :param bg_path: 保存路径
    :param bg_class: 背景图的 class 属性
    :return: 保存路径
    """
    bg_img_data = get_base64_by_canvas(driver, bg_class, False)
    save_base64img(bg_img_data, bg_path)
    return bg_path


def save_full_bg(driver, full_bg_path="fbg.png", full_bg_class="geetest_canvas_fullbg geetest_fade geetest_absolute"):
    """
    保存完整的的背景图
    :param driver: webdriver 对象
    :param full_bg_path: 保存路径
    :param full_bg_class: 完整背景图的 class 属性
    :return: 保存路径
    """
    bg_img_data = get_base64_by_canvas(driver, full_bg_class, False)
    save_base64img(bg_img_data, full_bg_path)
    return full_bg_path

def isElementExist(driver, elem_calss_name):
    try:
        driver.find_element_by_class_name(elem_calss_name)
        return True
    except:
        return False

class Crack():  
    def __init__(self, username, password):
        self.url = 'https://passport.bilibili.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 100)
        self.username = username
        self.password = password
        self.BORDER = 6

    def login(self):
        """
        打开浏览器并填入账号密码
        """
        self.browser.get(self.url)
        user_element = self.wait.until(EC.presence_of_element_located((By.ID, 'login-username')))
        pass_element = self.wait.until(EC.presence_of_element_located((By.ID, 'login-passwd')))
        user_element.clear()
        user_element.send_keys(self.username)
        pass_element.send_keys(self.password)

        login_btn = self.browser.find_element_by_class_name('btn-login')
        while not isElementExist(self.browser, 'geetest_canvas_bg geetest_absolute'):
            try:
                login_btn.click()
            except:
                break
        time.sleep(1)

    def is_pixel_equal(self, img1, img2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片的像素点
        pix1 = img1.load()[x, y]
        pix2 = img2.load()[x, y]
        threshold = 60
        if (abs(pix1[0] - pix2[0] < threshold) and abs(pix1[1] - pix2[1] < threshold) and abs(
                pix1[2] - pix2[2] < threshold)):
            return True
        else:
            return False

    def get_gap(self, img1, img2):
        """
        获取缺口偏移量
        :param img1: 不带缺口图片
        :param img2: 带缺口图片
        :return:
        """
        left = 50
        # 获取第一张图片的宽度  260 
        for i in range(left, img1.size[0]):
            # 获取第一张图片的高度
            for j in range(img1.size[1]):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    return left
        return left

    def get_track(self, distance):
        """
        读取移动轨迹并进行标准化
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
		# 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.12
        if distance > 110:
            t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:	
                # 加速度为负3
                a = -3.5
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append([round(move),random.choice([0,0,0,0,0,0,0,1])])
        return track
          

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        while True:
            try:
                slider = self.browser.find_element_by_class_name("geetest_slider_button")
                break
            except:
                time.sleep(0.5)
        time.sleep(1)
        return slider

    def move_to_gap(self, slider, track, distance):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        begin_time = time.time()
        ActionChains(self.browser).click_and_hold(slider).perform()
        track = track[::-1]
        for item in track:
            x = item[0]
            y = item[1]
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=y).perform()
        ActionChains(self.browser).release().perform()    
        end_time = time.time()
        print("exec_time: ", end_time - begin_time)

    def crack(self):
        # 打开浏览器
        self.login()

        # 保存滑动验证之前的图片
        bg_img = save_bg(self.browser)
        # 保存滑动验证成功之后的图片
        full_bg_img = save_full_bg(self.browser)

        gap = self.get_gap(image.open(full_bg_img), image.open(bg_img))
        print('缺口位置', gap)

        track = self.get_track(gap - self.BORDER)
        print('滑动滑块')
        print(track)

        # 点按呼出缺口
        slider = self.get_slider()

        # 拖动滑块到缺口处
        self.move_to_gap(slider, track, gap - self.BORDER)


if __name__ == '__main__':
    print('开始验证')
    password = getpass.getpass('PASSWORD:')
    crack = Crack("18667018590", 'b842549758')  # 账号密码
    crack.crack()
    print('验证完成')