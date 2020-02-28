"""
    京东爬虫
"""
import time

from selenium import webdriver

class JdSpider:
    def __init__(self):
        self.BaseUrl = 'https://www.jd.com/'
        self.browser = webdriver.Chrome()

    def parse_one_html(self):
        """
             解析一级页面： 1. 输入要查找的内容。点击。
                          2. 找到所有的链接（60）
        """
        self.browser.get(self.BaseUrl)
        user_input = input('请输入您要查找的内容：')
        # 输入框中填写输入内容
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys(user_input)
        # 点击
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()  
        time.sleep(1)
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(5)
        # 当前元素的节点是60个
        all_products = self.browser.find_elements_by_xpath('//li[@class="gl-item"]/div/div[1]/a/img')
        print('找到了%d个'%(len(all_products)))
        # 通过二级页面进行解析所有的商品数据
        self.parse_two_html(all_products)
    


    def parse_two_html(self,products):
        """
            此方法是用来解析二级页面
        """
        for each_product in products:
            each_product.click()
            self.browser.switch_to_window(self.browser.window_handles[1])
            # 手机的标题
            title = self.browser.find_element_by_xpath(
                '/html/body/div[8]/div/div[2]/div[1]'
                ).text.strip()
            # 手机的颜色
            colors = self.browser.find_element_by_xpath(
                '//*[@id="choose-attr-1"]/div[2]'
            ).text
            # 手机的规格
            types = self.browser.find_element_by_xpath(
                '//*[@id="choose-attr-2"]/div[2]'
            ).text
            # 图片的链接
            images_element = self.browser.find_elements_by_xpath(
                '//*[@id="spec-list"]/ul/li/img'
                ) # WebElement
            images = [ i.get_attribute('src') for i in images_element]
            print('title',title)
            print('color',colors)
            print('type',types)
            print('img',images)
            break

        time.sleep(10)

    def main(self):
        self.parse_one_html()
        self.browser.quit()

if __name__ == "__main__":
    jd = JdSpider()
    jd.main()

# 今日内容：
    # 1.京东爬虫
    # 2.b站滑动链登陆
    # # 7:30 开始
# https://img12.360buyimg.com/n5/s54x54_jfs/t1/102595/3/12610/144213/5e4cb782Ee6ce6e44/894d26bdcaaacbd3.jpg