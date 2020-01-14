"""
DAU
统计用户上线的天数
"""

import redis

redis_conn = redis.Redis()

# 用户1 一年中只活跃了第一天
redis_conn.setbit('user:1',0,1)

# user:2 活跃150填以上的用户
# for i in range(0,365,2):
#     redis_conn.setbit('user:2',i,1)


# 设置全年活跃
# for i in range(0,365):
#     redis_conn.setbit('user:3',i,1)

# bitcount key start end （字节的位数） 
#  全年获取少于100 天

# for i in range(0,365,4):
#     redis_conn.setbit('user:4',i,1)

active = []
unactive = []

res = redis_conn.keys('*')
for i in res:
    count = redis_conn.bitcount(i)
    if count > 100:
        active.append(i)
    else:
        unactive.append(i)
print('活跃用户',active)
print('un活跃用户',unactive)
