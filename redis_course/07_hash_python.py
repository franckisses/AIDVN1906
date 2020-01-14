import redis

redis_conn = redis.Redis()



# 存储单个字段
# redis_conn.hset('user:7','username','xiaowang')

# 存入多个字段
dic = {
    'username':'xiali',
    'ido':'kobe,messi',
    'hobby':'football'
}
# redis_conn.hmset('user:8',dic)

# 拿出所有的字段和值
print(redis_conn.hgetall('user:8'))

# 拿出所有的值
print(redis_conn.hvals('user:8'))\
    
# 9:05