
"""
DATETIME: 2020 02 10 21:30
Author: franck
Email: franck_gxu@outlook.com
"""
#(base) Franck:day03 gongyan$ touch mysqlhelper.py
import pymysql


class DatabaseHelper:
    """
        完成所有的对于mysql的操作
    """
    def __init__(self,host='localhost',port=3306,user='root',
    password='123456',database=None,charset='utf8'):
        self.host = host
        self.port = port 
        self.password = password
        self.database = database
        self.user = user
        self.charset = charset
        self.conn = None
        self.cur = None
    
    def connectdatabase(self):
        """
            用来定义链接数据库：return : True/False
        """
        try:
            self.conn = pymysql.connect(
                host = self.host,
                user = self.user,
                port = self.port,
                password = self.password,
                database = self.database,
                charset = self.charset 
            )
        except Exception as e:
            print('[链接数据库失败]:',e)
            return False
        self.cur = self.conn.cursor()
        print(self.conn)
        print(self.cur)
        return True
    
    def close(self):
        """
            关闭数据库的链接： 先关闭游标对象再关链接对象
        """
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        return True
    
    def execute(self,sql,params=None):
        if self.connectdatabase() == False:
            return False
        try:            
            if self.conn and self.cur:
                self.cur.execute(sql,params)
                self.conn.commit()
        except Exception as e:
            print('[插入失败]:',e)
            return False
        return True
    
    # TODO 自己实现executemany(sql,param_list)
    # 判断每一个元素是否为元祖。
    # 再去调用executemany这个方法

if __name__ == "__main__":
    db = DatabaseHelper(database='maoyan')
    sql = 'insert into maoyan_board values(%s,%s,%s,%s,%s)'
    movies_detail = ['http://www.baidu.com','寄生虫','韩国人','2019-10-11','9.3']
    if db.execute(sql,params=movies_detail):
        print('数据插入成功')
    print(db.close())
    
        