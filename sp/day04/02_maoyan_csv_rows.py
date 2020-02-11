
from urllib import request
from fake_useragent import UserAgent
import re
import time
import csv

import pymysql

class MaoyanSpider:
    def __init__(self):
        self.url = "https://maoyan.com/board/4?offset={}"

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
        # TODO 实现单行的写入 writerows([(),(),(),()])
        # 图片 电影名  主演 上映时间 评分
        #('https://p0.meituan.net/movie/ce4da3e03e655b5b88ed31b5cd7896cf62472.jpg@160w_220h_1e_1c', 
        # '霸王别姬', '\n                主演：张国荣,张丰毅,巩俐\n        ', 
        # '上映时间：1993-07-26', '9.', '5')
        # 这是每一页中电影的数据格式
        page_data = []      
        for i in all_list:
            # 这是每一个电影的构造数据格式
            each_movie = (i[0].split('@')[0], i[1], i[2].strip()[3:],
            i[3][5:15], i[4] + i[5])
            page_data.append(each_movie)
            
        with open('maoyan_board1.csv','a') as f: # w 
            writer = csv.writer(f)
            writer.writerows(page_data)


    def main(self):
        for i in range(0,100,10):
            url = self.url.format(i)
            self.get_html(url)
            time.sleep(1.5)

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
# truncate table 表名
# 将表中的数据清除


