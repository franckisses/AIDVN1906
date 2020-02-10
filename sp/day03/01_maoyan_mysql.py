
from urllib import request
from fake_useragent import UserAgent
import re

import pymysql

class MaoyanSpider:
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset={}"
        pymysql.connect('127.0.0.1','root','123456','database',
        '3306',chrset='utf8')
        # database:  maoyan
        # table: maoyan_board

    def get_html(self,current_url):
        headers = {
            'User-Agent': UserAgent().firefox
        }
        res_obj = request.Request(current_url,headers=headers)
        response = request.urlopen(res_obj)
        html = response.read().decode()
        self.parse_html(html)



    def parse_html(self,html):
        pattern = re.compile('<img data-src="(.*?)".*?<div class="movie-item-info".*?title="(.*?)".'
                         '*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>.*?class="integer">'
                             '(.*?)</i>.*?fraction">(.*?)</i>',re.S)
        re_list = pattern.findall(html)
        print('下面是正则表达式匹配出的内容：\n',re_list)
        self.write_html(re_list)

    def write_html(self,all_list):
        data = []
        for i in all_list:
            movie = {}
            movie['img'] = i[0].split("@")[0]
            movie['title'] = i[1]
            movie['actor'] = i[2].strip()[3:]
            movie['public'] = i[3].strip()[5:15]
            movie['score'] = i[4] + i[5]
            # print(movie)
            data.append(movie)
        # print(data)
    #　TODO 类　封装成一个工具　mysql
    # pymysyql
    # a = MysqlHelper(host,db,port,password)
    # listhelper
    # a.insert('insert ******',[name,age,score])
    # a.select()



    def main(self):
        for i in range(0,10,10):
            url = self.url.format(i)
            self.get_html(url)

if __name__ == '__main__':
    maoyan = MaoyanSpider()
    maoyan.main()

# 创建数据库
# mysql> create database maoyan default charset utf8;
# Query OK, 1 row affected (0.00 sec)
# mysql> use maoyan;   
# # 创建表
# mysql> create table maoyan_board(
#     -> img varchar(300),
#     -> title varchar(30),
#     -> star varchar(50),
#     -> public varchar(10),
#     -> score varchar(3)) charset=utf8;                                                                                   Database changed
# Query OK, 0 rows affected (0.02 sec)

# desc maoyan_board;

