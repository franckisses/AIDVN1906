"""
用户修改个人信息时，要将数据同步到redis缓存
"""
import redis
import pymysql



class Update:
    def __init__(self):
        self.redis_conn = redis.Redis()
        self.mysql_conn = pymysql.connect(host='localhost', user='root', password='123456',
                 database='blog', port=3306,charset='utf8')
        self.cursor = self.mysql_conn.cursor()

    def update_mysql(self,username,email):
        sql = 'update user set email=%s where username=%s'
        try:
            code = self.cursor.execute(sql,[email,username])
        except Exception as e:
            self.mysql_conn.rollback()
            print("更新失败:",e)
        if code:
            self.mysql_conn.commit()
            return True
        
    def update_redis(self,username,email):
        self.redis_conn.hset(username,'email',email)
        self.redis_conn.expire(username,60*60)
    
    def main(self):
        username = input('username:')
        email = input('email:')
        if self.update_mysql(username,email):
            self.update_redis(username,email)
            print('数据更新成功！')
        else:
            print('未修改！')
if __name__ == "__main__":
    up = Update()
    up.main()