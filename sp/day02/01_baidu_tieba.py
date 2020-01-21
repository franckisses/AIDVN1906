
from urllib import request,parse



class BaiduTiebaSpider:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
    def build_url(self):
        keyword = input('请输入您要查看的贴吧名：')
        page = input('请输入下载多少页[默认从第1页开始]')
        # TODO 自己写默认值
        # 将字符串转换为url编码值
        keyword_encode = parse.quote(keyword)
        # 构造每一页的url
        for i in range(0,50*page,50):
            return self.url.format(keyword_encode,i)

    def get_page(self):
        pass
    def write_page(self):
        pass
    def main(self):
        url = self.build_url()

if __name__ == '__main__':
    s = BaiduTiebaSpider()
    s.main()





