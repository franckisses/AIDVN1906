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
        all_products = self.browser.find_elements_by_xpath('//li[@class="gl-item"]/div/div[1]/a/img')
        print('找到了%d个'%(len(all_products)))
        for i in all_products:
            # WebElement.get_attribute('class') # pn-next / pn-next disable
            print(i.get_attribute('src'))
            # time.sleep(10)
            # print(self.browser.window_handles)
            break
        # print(all_products)
        # print(len(all_products))


    def parse_two_html(self):
        pass

    def main(self):
        self.parse_one_html()
        self.browser.quit()

if __name__ == "__main__":
    jd = JdSpider()
    jd.main()