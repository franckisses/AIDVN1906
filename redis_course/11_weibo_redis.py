import redis

r = redis.Redis(host='127.0.0.1',port=6379,db=0)

# user1关注的人
r.sadd('user1:focus','peiqi','qiaozhi','danni')
# user2关注的人
r.sadd('user2:focus','peiqi','qiaozhi','lingyang')
# 共同关注: 求交集 {b'qiaozhi', b'peiqi'}
focus_set = r.sinter('user1:focus','user2:focus')

# 创建空集合,存放最终结果
result = set()

for focus in focus_set:
  result.add(focus.decode())

print(result)