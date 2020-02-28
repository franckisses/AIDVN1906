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
        status = 0 
        while status in (0,1):
            all_products = self.find_elements_in_current_page()
            # 通过二级页面进行解析所有的商品数据
            self.parse_two_html(all_products)
            # 获取下一页的元素
            a_tag = self.browser.find_element_by_xpath(
                '//*[@id="J_bottomPage"]/span[1]/a[9]'
                )
            # 获取下一页元素的属性
            a_status = a_tag.get_attribute('class')
            # 判断元素是否可以点击
            if 'disabled' not in a_status:
                a_tag.click()
                time.sleep(2)
            else:
                if status == 1:
                    break
                status = 1

    def find_elements_in_current_page(self):
        time.sleep(5)
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
        all_products = self.browser.find_elements_by_xpath('//li[@class="gl-item"]/div/div[1]/a/img')
        print(len(all_products))
        return all_products

    def parse_two_html(self,products):
        """
            此方法是用来解析二级页面
        """
        for index,each_product in enumerate(products):
            print('current:',index+1)
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
            images = [ i.get_attribute('src') for i in images_element ]
            print('title',title)
            print('color',colors)
            print('type',types)
            print('img',images)
            print('--------------------')
            # 关闭第二个选项卡
            time.sleep(2)
            self.browser.close()
            # 将选项卡切换回第一个
            self.browser.switch_to_window(self.browser.window_handles[0])
            time.sleep(1)

        # time.sleep(10)

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