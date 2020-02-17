"""
name: fightpic.py
datetime: 2020-02-17 20:07
"""

import requests
from fake_useragent import UserAgent
from lxml import etree
from urllib import request

import time
import random
import os

PIC_PATH = './fightpic'

class FightPic:
    def __init__(self):
        self.Baseurl = 'https://www.doutugou.net/category/dashijian/page/{}'
        self.headers = {
            'User-Agent':UserAgent().random
        }
    
    def parse_html(self,url):
        """解析页面"""
        html = self.get_html(url)
        text = etree.HTML(html)
        all_imgs = text.xpath('//div[@class="thumbnail"]/a/img')
        each_page = {}
        for i in all_imgs:
            # 保存格式 {'nihao zhongguo ':'http://baidu.com',} 
            each_page[i.xpath('./@alt')[0]] = i.xpath('./@src')[0]
        self.save_pic(each_page)



    def get_html(self,url):
        """页面下载函数"""
        try:
            response = requests.get(url=url,headers=self.headers)
        except Exception as e:
            print('[Error]:',e)
        else:
            return response.text

    def save_pic(self,page_pic):
        """保存图片"""
        print('开始保存图片')
        # 将图片存入到指定的文件夹中
        if not os.path.exists(PIC_PATH):
            os.makedirs('fightpic')
        for key,value in page_pic.items():
            # ['丽芙流光表情包#斗图大事件#20191211']
            name = key.split('#')[0]
            try:
                print('start downloading%s....'%name)
                request.urlretrieve(value,PIC_PATH+'/'+name+value[-4:])
                print('download over%s.'%name)
            except Exception as e:
                print('[Error]:',e)


    def main(self):
        """爬虫启动方法"""
        for i in range(1,49):
            current_url = self.Baseurl.format(i)
            print('开始下载第%d页的数据,当前的URL是:%s'%(i,current_url))
            self.parse_html(current_url)
            time.sleep(random.randint(1,3))
            break

if __name__ == "__main__":
    pic = FightPic()
    pic.main()



"""
https://img.doutugou.net/2020/02/9150e4e5gy1fx4k6v0iilj20c80g9woe.jpg
https://img.doutugou.net/2020/02/9150e4e5gy1gbw82nxyudj204g03o743.jpg
https://img.doutugou.net/2020/02/9150e4e5gy1gbw5zx4jslj208e08a0su.jpg
https://img.doutugou.net/2020/02/9150e4e5gy1gbuftxih2wj20u00u0gs3.jpg
https://img.doutugou.net/2020/02/20200212473901_NKekBz.png
https://img.doutugou.net/2020/02/20200212474251_qSDinP.jpg
https://img.doutugou.net/2020/02/6af89bc8gw1f8pi28bd1rj207e06bq31.jpg
https://img.doutugou.net/2020/02/9150e4e5gy1gbouue18s6g206o06odfo.gif
https://img.doutugou.net/2020/02/9150e4e5gy1gbntlesbynj20b10aztb5.jpg
https://img.doutugou.net/2020/02/9150e4e5gy1gbnttiwibag208c08c751.gif
https://img.doutugou.net/2020/02/9150e4e5gy1gbmi4l8py3g206o06owil.gif
https://img.doutugou.net/2020/02/9150e4e5gy1gblgpy0iqyg20c50e57al.gif
https://img.doutugou.net/2020/02/9150e4e5gy1gbhxqqehlaj20v70y6tc7.jpg
https://img.doutugou.net/2020/01/37818616.gif
https://img.doutugou.net/2020/01/9150e4e5gy1gb9vg6zwnuj20hs0hs0td.jpg
https://img.doutugou.net/2020/01/006CIHwQgy1gb87ns1a0bj30rs0rstl7.jpg
https://img.doutugou.net/2020/01/9150e4e5ly1fu3tnrshu4j20hs0hswfg.jpg
https://img.doutugou.net/2020/01/9150e4e5gy1gazoc4jngnj206o06ot8l.jpg
https://img.doutugou.net/2020/01/006dMd5bgy1gb1pl60rcsg303d03cq4z.gif
https://img.doutugou.net/2020/01/9150e4e5gy1gawga3fsivg206o06oglw.gif
https://img.doutugou.net/2020/01/814268e3gy1gavb0bu3qag208c08c750.gif
https://img.doutugou.net/2020/01/9150e4e5gy1gau5u2mg77g201e01ewef.gif
https://img.doutugou.net/2020/01/9150e4e5gy1gascx2kd2tj20fo0fotg4.jpg
https://img.doutugou.net/2020/01/20200110613330_RLmHXS.gif
https://img.doutugou.net/2020/01/9150e4e5gy1gaoukg0jxlg2046046gng.gif
https://img.doutugou.net/2020/01/9150e4e5gy1gam2f7ad1ig203f035aad.gif
https://img.doutugou.net/2020/01/006cSBLKgy1gakdef1jalj306o06o74j.jpg
https://img.doutugou.net/2020/01/9150e4e5gy1gagpw0pxb6j20m80m8dho.jpg
https://img.doutugou.net/2019/12/9150e4e5gy1gafmi0840pg206o06o40z.gif
https://img.doutugou.net/2019/12/9150e4e5gy1gadbgffxblj20j60j60tt.jpg
https://img.doutugou.net/2019/12/006BkP2Hly1fmpwzrvw1pj308c08cglx.jpg
https://img.doutugou.net/2019/12/9150e4e5gy1ga7ijagwiwg206o06ojtw.gif
https://img.doutugou.net/2019/12/20191223062661_VEHPkK.gif
https://img.doutugou.net/2019/12/d827932dly1ga5hl04d8jg20gf0cb7ag.gif
https://img.doutugou.net/2019/12/20191221883868_wJeWpN.gif
https://img.doutugou.net/2019/12/20191219710910_MjcqZh.gif
https://img.doutugou.net/2019/12/20191218624512_hatZPE.gif
https://img.doutugou.net/2019/12/20191217538573_zkdspD.jpg
https://img.doutugou.net/2019/12/20191215403350_xIBfsy.gif
https://img.doutugou.net/2019/12/20191211993939_OvkSHU.jpg
https://img.doutugou.net/2019/12/20191206588307_IScUOn.gif
https://img.doutugou.net/2019/12/20191205503762_XcbgLP.gif
"""