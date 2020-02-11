
from urllib import request,parse
from fake_useragent import UserAgent

import time

class BaiduTiebaSpider:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
    def build_url(self):
        keyword = input('请输入您要查看的贴吧名：')
        page = int(input('请输入下载多少页[默认从第1页开始]'))
        # TODO 自己写默认值
        # 将字符串转换为url编码值
        keyword_encode = parse.quote(keyword)
        # 构造每一页的url
        for i in range(0,50*page,50):
            url = self.url.format(keyword_encode,i)
            self.get_page(url,'%s吧的第%d页'%(keyword,i))

    def get_page(self,each_url,filename):
        # 构造请求头
        headers = {
            'User-Agent':UserAgent().chrome
        }
        # 构造请求对象
        print('start download',filename)
        res_obj = request.Request(each_url,headers=headers)
        # 接受返回的响应
        response = request.urlopen(res_obj)
        # 讲返回的响应 生成文本字符串
        html = response.read().decode()
        self.write_page(html,filename)

    def write_page(self,html,filename):
        with open(filename,'w') as f:
            f.write(html)
        print('保存完毕',filename)

    def main(self):
        self.build_url()

        # self.get_page(url)

if __name__ == '__main__':
    s = BaiduTiebaSpider()
    start = time.time()
    s.main()
    print(time.time() - start)




#http://tieba.baidu.com/f?ie=utf-8&kw=%E8%82%BA%E7%82%8E&red_tag=n3531408564&pn=0
http://tieba.baidu.com/f?kw=%E5%8C%97%E4%BA%AC&ie=utf-8&cid=&tab=corearea&pn=50