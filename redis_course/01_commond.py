# 安装redis模块
#　sudo pip3 install redis

import redis

redis_conn = redis.Redis()


# print(redis_conn.keys('*'))
# 拿出所有的键
# for i in redis_conn.keys():
#     print(i.decode())


# 查看类型
# print(redis_conn.type('name1'))

# 键值对是否存在
# print(redis_conn.exists('name1')) # 1 
# print(redis_conn.exists('name1123')) # 0



# print(redis_conn.delete('name1'))

# 对于字符串的操作：
redis_conn.set('name','xiaowang')
# 存储多个值
dic = {
    'age': 18,
    'gender':'F',
    'score':100
}
redis_conn.mset(dic)
# 获取键值对
print(redis_conn.get('name').decode())

print(redis_conn.mget('name','age','gender'))

# 设置记录小王粉丝数量的字符串
redis_conn.set('user:xiaoawangfans',0)
# 对小王的粉丝数量进行加1  执行三次
for i in range(3):
    redis_conn.incr('user:xiaowangfans')

# 对小王的粉丝的数量进行减2 
redis_conn.decrby('user:xiaowangfans',2)




