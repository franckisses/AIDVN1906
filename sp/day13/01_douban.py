"""
    豆瓣爬虫代码：
        获取豆瓣电影数据
"""
import requests
import re
from lxml import etree
# pip3 install lxml
import time
import csv
from fake_useragent import UserAgent


class DoubanSpider:
    def __init__(self):
        self.headers = {
            'User-Agent' : UserAgent().random
        }
        self.url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'

    def parse_html(self,current_url):
        """解析页面的函数"""
        html = self.get_html(current_url)
        html_josn = html.json()
        # TODO 将这些数据存入到csv中 writerows() 
        all_data = [] 
        # [(),(),()]
        for each_movie in html_josn:
            each_data =(
                each_movie['rank'],
                " ".join(each_movie["types"]),
                " ".join(each_movie["regions"]),
                each_movie["title"],
                each_movie["url"],
                each_movie["release_date"],
                each_movie["vote_count"],
                each_movie["score"],
                "、".join(each_movie["actors"])
            )
            all_data.append(each_data)
        with open('douban.csv','a') as f:
            writer = csv.writer(f)
            writer.writerows(all_data)
  
    def get_html(self,current_url):
        """发送请求"""
        try:
            response = requests.get(
                url=current_url,
                headers=self.headers 
            )
        except Exception as e:
            print('[Error]:',e)
        else:
            return response

    def get_types(self):
        url = 'https://movie.douban.com/chart'
        html = self.get_html(url).text
        regex_exp = '<a href="/typerank.*?type=(.*?)&.*?">(.*?)</a>' 
        pattern = re.compile(regex_exp, re.S)
        result = pattern.findall(html)
        # [(),()]
        return dict(result)

    def get_total(self,movie_type):
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'
        response = self.get_html(url.format(movie_type))
    
        return response.json()['total']

    
    def main(self):
        type_list = self.get_types()
        print('-------------------------------------')
        print('|    请根据数字选择要下载的数据       |')
        for key,value in type_list.items():
            print('|'+(key+":"+value).center(35-len(key+":"+value))+'|')
        print('-------------------------------------')
        userInput = input('请输入您要下载的电影数据编号:')
        # 此方法是用来获取当前电影类型的总数
        total = self.get_total(userInput)
        for start in range(0,total,20):
            url = self.url.format(userInput,start)
            # print(url)
            self.parse_html(url)
            break

            

if __name__ == "__main__":
    douban = DoubanSpider()
    douban.main()

"""
{
    "rank":67, # 在同一类型中的排名
    "types":["科幻","悬疑","惊悚"],
    "regions":["德国","美国"],
    "title":"异次元骇客",
    "url":"https:\/\/movie.douban.com\/subject\/1300282\/",
    "release_date":"1999-05-28",
    "actor_count":26,
    "vote_count":72429,
    "score":"8.4",
    "actors":["克雷格·比尔克","阿明·缪勒-斯塔尔","格瑞辰·摩尔","文森特·多诺费奥","丹尼斯·海斯伯特","斯蒂文·沙博","里夫·霍顿","珍妮特·麦克拉克伦","布拉德·威廉姆·亨克","蒂娅·德克萨达","莱昂·里皮","伯特·布洛斯","霍华德·S·米勒","威尔·华莱士","李韦弗","Travis Tedford","艾莉森·洛曼","施瑞·阿普莱碧","Ernie Lively","鲍勃·克莱德宁","Brooks Almy","Jeff Blumenkrantz","Toni Sawyer","Tracy Perry","约翰尼·克劳福德","Hadda Brooks"],
}
# """
# <a href="/typerank?type_name=剧情&amp;type=11&amp;interval_id=100:90&amp;action=">剧情</a>
# <a href="/typerank?type_name=喜剧&amp;type=24&amp;interval_id=100:90&amp;action=">喜剧</a>
# <a href="/typerank.*?type=(.*?)&.*?">(.*?)</a>