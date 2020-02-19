
import os
import requests
from fake_useragent import UserAgent
from lxml import etree
from urllib import request
# tarenacode
# code_2013
# http://code.tarena.com.cn/AIDCode/aid1907/11-Ajax/

FILEPATH = './mynote'

class TarenaCode:
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid1907/11-Ajax/' 
        self.auth = ('tarenacode','code_2013')
        self.headers = {
            'User-Agent': UserAgent().random
        }

    def parse_html(self):
        """解析网页"""
        html = self.get_html()
        text = etree.HTML(html)
        a_list = text.xpath('//a/@href') 
        # ['day01/','day02/','mytest.zip']
        print(a_list)
        myfile = [ i for i in a_list if '/' not in i]
        print(myfile)
        self.save_file(myfile)


    def get_html(self):
        """下载网页"""
        try:
            response = requests.get(
                url=self.url,
                auth=self.auth,
                headers = self.headers
            )
        except Exception as e:
            print('[error]:',e)
        else:
            return response.text

    def save_file(self,files):
        """保存文件"""
        if not os.path.exists(FILEPATH):
            os.makedirs('mynote')
        for each_file in files:
            file_url = self.url + each_file 
            binary_file = requests.get(file_url,auth=self.auth,headers=self.headers).content
            with open(FILEPATH+'/'+each_file,'wb') as f:
                f.write(binary_file)
            print(each_file,'下载成功！')


    def main(self):
        """主方法，用来启动爬虫"""
        self.parse_html()

if __name__ == "__main__":
    tc = TarenaCode()
    tc.main()


"""
<a href="day01/">day01/</a>                                             28-Oct-2019 21:27       -
<a href="day02/">day02/</a>                                             28-Oct-2019 21:27       -
<a href="day03/">day03/</a>                                             29-Oct-2019 17:26       -
<a href="practice/">practice/</a>                                          30-Oct-2019 18:17       -
<a href="day01-note.zip">day01-note.zip</a>                                     24-Oct-2019 23:57    499K
<a href="day03-note.zip">day03-note.zip</a>                                     28-Oct-2019 22:38    343K
<a href="day03_all.zip">day03_all.zip</a> 

"""
# <a href="(.*?)">(.*?)</a>