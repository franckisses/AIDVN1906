import redis
import time 
from multiprocessing import Process

REDDIS_CONN = redis.Redis()

class SpiderConsumeProduct:

    def product(self):
        for i in range(1,11):
            url = 'https://bj.lianjia.com/ershoufang/pg{}/'.format(i)
            REDDIS_CONN.lpush('lianjia:ershoufang1',url)
            time.sleep(1)

    def consumer(self):
        while True:
            url = REDDIS_CONN.blpop('lianjia:ershoufang1',10)
            if url:
                print('正在抓取的url为%s'%url[0].decode())
            else:
                print('没有资源了！')
                break
    def main(self):
        p01 = Process(target=self.product)
        p02 = Process(target=self.consumer)

        p01.start()
        p02.start()
        p01.join()
        p02.join()


if __name__ == "__main__":
    s = SpiderConsumeProduct()
    s.main()
