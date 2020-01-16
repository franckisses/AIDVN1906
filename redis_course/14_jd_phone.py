"""
# 第1天
ZADD mobile-001 5000 'huawei' 4000 'oppo' 3000 'iphone'
# 第2天
ZADD mobile-002 5200 'huawei' 4300 'oppo' 3230 'iphone'
# 第3天
ZADD mobile-003 5500 'huawei' 4660 'oppo' 3580 'iphone'

"""
import redis
redis_conn = redis.Redis()

day01 = {
    'huawei':5000,
    'oppo':4000 , 
    'iphone':3000 
}


day02 = {
    'huawei':4000,
    'oppo':4100 , 
    'iphone':3600 
}

day03  = {
    'huawei': 10000,
    'oppo': 5000 , 
    'iphone': 12000 
}

redis_conn.zadd('mobile:day01',day01)
redis_conn.zadd('mobile:day02',day02)
redis_conn.zadd('mobile:day03',day03)

# 
redis_conn.zunionstore('mobile:salecount',(
    'mobile:day01',
    'mobile:day02',
    'mobile:day03'
    )
)
# print(redis_conn.zrange('mobile:salecount',0,2,withscores=True))
for index,value in enumerate(redis_conn.zrange(
    'mobile:salecount',0,2,withscores=True),1):
    # print(index,value)
    print('销量排名第{}的品牌是{}，销量为{}'.format(
        index,value[0].decode(),value[1]))
