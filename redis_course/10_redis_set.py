import redis

r = redis.Redis()
# 1、给name对应的集合中添加元素

# sadd(name,values)
print(r.sadd("set_name","tom"))
print(r.sadd("set_name","tom","jim"))

# 2、获取name对应的集合的所有成员: python集合
# smembers(name)
print(r.smembers('setname'))
# print(r.smembers('set_name'))

# 3、获取name对应的集合中的元素个数
# scard(name)
print(r.scard("set_name"))

# 4、检查value是否是name对应的集合内的元素:True|False
# sismember(name, value)
print(r.sismember('set_name','tom'))

# 5、随机删除并返回指定集合的一个元素
# spop(name)
print(r.spop('set_name'))

# 6、删除集合中的某个元素
# srem(name, value) 
print(r.srem("set_name", "tom"))

# 7、获取多个name对应集合的交集
# sinter(keys, *args)

r.sadd("set_name","a","b")
r.sadd("set_name1","b","c")
r.sadd("set_name2","b","c","d")

print(r.sinter("set_name","set_name1","set_name2"))
#输出:｛b'b'｝

# 8、获取多个name对应的集合的并集: python集合
# sunion(keys, *args)
print(r.sunion("set_name","set_name1","set_name2"))