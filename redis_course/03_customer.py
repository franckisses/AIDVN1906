# 消费者模型
import redis

redis_conn = redis.Redis()


while True:
    url = redis_conn.blpop('lianjia:ershoufang',5)
    if url:
        print('正在抓取的url为%s'%url[0].decode())
    else:
        print('没有资源了！')
        break