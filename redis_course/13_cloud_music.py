
import redis


redis_conn = redis.Redis()


# myFavMus = {
#     'fake': 1000,
#     'you are beautiful':500,
#     'happy birthday':10000
# }


# redis_conn.zadd('songs:rank',myFavMus)

# 模拟用户播放：
redis_conn.zincrby('songs:rank',20,'fake')
redis_conn.zincrby('songs:rank',10,'happy birthday')

musicbyplay =  redis_conn.zrevrange("songs:rank",0,2,withscores=True)

# print(musicbyplay)
for index,value in enumerate(musicbyplay,1):
    print(index,value)
    print('排名第{}的歌曲是{}，播放量为：{}.'.format(
        index,value[0].decode(),value[1])
        )




    
