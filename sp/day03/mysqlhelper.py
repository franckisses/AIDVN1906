
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
    
    def connectatabase(self):
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

if __name__ == "__main__":
    db = DatabaseHelper(database='maoyan')
    print(db.connectatabase())

        