import redis

r = redis.Redis()
# 注意第二个参数为字典
# 命令行:ZADD salary 6000 tom 8000 jim
r.zadd('salary',{'tom':6000,'jim':8000,'jack':12000})
# # 结果为列表中存放元组[(),(),()]
print(r.zrange('salary',0,-1,withscores=True))
# print(r.zrevrange('salary',0,-1,withscores=True))
# # start:起始值,num:显示条数
print(r.zrangebyscore('salary',6000,12000,start=1,num=2,withscores=True))
# # 删除
r.zrem('salary','tom')
print(r.zrange('salary',0,-1,withscores=True))
# # 增加分值
r.zincrby('salary',5000,'jack')
print(r.zrange('salary',0,-1,withscores=True))
# # 返回元素排名
print(r.zrank('salary','jack'))    # 正序排名
print(r.zrevrank('salary','jack')) # 逆序排名
# # 删除指定区间内的元素
r.zremrangebyscore('salary',6000,8000)
print(r.zrange('salary',0,-1,withscores=True))
# # 统计元素个数
print(r.zcard('salary'))
# # 返回指定范围内元素个数
print(r.zcount('salary',6000,20000))
# # 并集
r.zadd('salary2',{'jack':17000,'lucy':8000})
r.zunionstore('salary3',('salary','salary2'),aggregate='max')
print(r.zrange('salary3',0,-1,withscores=True))
# # 交集
r.zinterstore('salary4',('salary','salary2'),aggregate='max')
print(r.zrange('salary4',0,-1,withscores=True))