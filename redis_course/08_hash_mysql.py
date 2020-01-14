"""
用户想要查询个人信息
    1、到redis缓存中查询个人信息
    2、redis中查询不到，到mysql查询，并缓存到redis
    3、再次查询个人信息
"""
import redis
import pymysql


redis_conn = redis.Redis()
mysql_conn = pymysql.connect(host='localhost', user='root', password='123456',
                 database='blog', port=3306,charset='utf8')
cursor = mysql_conn.cursor()
username = input('用户名：')
result = redis_conn.hgetall(username)
if result:
    print('this result from redis:',result)
else:
    sql = 'select nickname,email from user where username=%s'
    affected = cursor.execute(sql,[username]) 
    if not affected:
        print('查无此人')
    else:
        userinfo = cursor.fetchone() # ()
        print('this result from mysql:',userinfo)
        redis_conn.hmset(username,{'nickname':userinfo[0],'email':userinfo[1]})
        redis_conn.expire(username,60*60)




