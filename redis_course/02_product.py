# 生产者模型
import redis
import time
redis_conn = redis.Redis()


for i in range(1,11):
    url = 'https://bj.lianjia.com/ershoufang/pg{}/'.format(i)
    redis_conn.lpush('lianjia:ershoufang',url)
    time.sleep(1)
