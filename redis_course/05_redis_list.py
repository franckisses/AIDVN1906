
import redis


redis_conn = redis.Redis()



# redis_conn.lpush('list01',1,2,3,4,5,6,7,9)

print(redis_conn.lrange('list01',0,-1))

for i in redis_conn.lrange('list01',0,-1):
    print(i.decode())

# 插入值：
# redis_conn.linsert('list01','after',9,'我爱你中国')

#弹出元素：
print(redis_conn.lpop('list01'))
print(redis_conn.lpop('list01'))


redis_conn.expire('list01',10)

