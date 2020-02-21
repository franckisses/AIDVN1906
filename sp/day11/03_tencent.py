"""
    tencent spider
"""
import random 
import json
import requests 
from fake_useragent import UserAgent


class TencentHireSpider:
    def __init__(self):
        self.base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={}&pageSize=10&countryId=1'
        self.detail_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?&postId={}'
        self.headers = {
            'User-Agent':UserAgent().random,
            'cookie': '_ga=GA1.2.2044289726.1580734942; pgv_pvi=4707361792; _gcl_au=1.1.1282525445.1580734943; loading=agree'
        }
    
    def get_json(self,current_url):
        try:
            response = requests.get(
                url = current_url,
                headers = self.headers 
            )
        except Exception as e:
            print('[Error]:',e)
            return None
        else:
            return response.json()   
    def get_position_url(self,current_url):
        position_dict = self.get_json(current_url)
        if position_dict:
            for i in position_dict['Data']['Posts']:
                positionId = i['PostId']
                print('正在抓取职位的id是:',positionId)
                self.get_position_detail(positionId)
    def get_position_detail(self,current_id):
        # TODO 存储职位信息
        position_url = self.detail_url.format(current_id)
        position_detail = self.get_json(position_url)
        if position_detail:
            print(position_detail)
    
    def main(self):
        print('Tencent Spider Starting work....')
        for i in range(1,449):
            print('---开始爬取第%d页---'%i)
            url = self.base_url.format(i) 
            self.get_position_url(url)
            break     


if __name__ == "__main__":
    tx = TencentHireSpider()
    tx.main()


# # 获取所有职位信息的链接
# https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={}&pageSize=10&countryId=1
# 在此链接之下可以获取到每一个页面的postid
# # 获取岗位详情的链接 

# PostId = 
# https://careers.tencent.com/tencentcareer/api/post/ByPostId?&postId=1123175622420467712