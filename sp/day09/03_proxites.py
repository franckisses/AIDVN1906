"""
    代理IP获取并测试生成可用代理池
"""
import requests
import time
from lxml import etree
from fake_useragent import UserAgent

IPPOOL = 'ippool.txt'

class IPTest:
    def __init__(self):
        self.IPaddress = 'https://www.kuaidaili.com/free/inha/{}'
        self.headers = {
            'User-Agent': UserAgent().random
        }
        self.proxies = {
            'http':'http://47.92.233.42:16818',
            'https':'https://47.92.233.42:16818'
        }
    def parse_html(self,url):
        """ 解析快代理网页"""
        html = self.get_html(url)
        text = etree.HTML(html)
        tr_list = text.xpath('//tbody/tr')
        print('tr_list',tr_list)
        all_proxies = {}
        for i in tr_list:
            all_proxies[i.xpath('./td[1]/text()')[0]] = i.xpath('./td[2]/text()')[0]
        self.test_ip(all_proxies)

    def get_html(self,current_url):
        """
        获取快代理网页
        return str
        """
        try:
            response = requests.get(
                url=current_url,
                headers = self.headers,
                proxies = self.proxies
            )
        except Exception as e:
            print('[Error]:',e,'当前的URL为：%s'%current_url)
        else:
            return response.text

    def test_ip(self,proxies):
        """
        测试代理IP可用性
        可以用保存起来 httpbin.org/get 
        """
        for ip,port in proxies.items():
            test_url = 'http://www.baidu.com'
            proxies = {
                'http':'http://{}:{}'.format(ip,port),
                'https':'https://{}:{}'.format(ip,port)
            }
            try:
                response = requests.get(
                    url=test_url,
                    proxies=proxies,
                    timeout=4
                    )
                if response.status_code == 200:
                    print('[Success]:',ip,port)
                    with open(IPPOOL,'a') as f:
                        f.write(str(ip)+":"+str(port)+'\n')
            except Exception as e:
                print('[Failed]:',ip,port)

        # 可以通过response.status_code == 200  
        pass
    def main(self):
        print('start visit kuaidaili.......')
        for i in range(2,51):
            print('当前页面时第%d页'%i)
            url = self.IPaddress.format(i)
            self.parse_html(url)



if __name__ == "__main__":
    ip = IPTest()
    ip.main()



