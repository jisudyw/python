import pymysql
from common.config import ReadConfig
from common import contains

class MysqlUntil:
    get_conf = ReadConfig()
    def __init__(self):
        # self.config.read(contains.conf_global, encoding='utf-8')
        host = self.get_conf.get('db', 'host')
        user = self.get_conf.get('db', 'user')
        password = self.get_conf.get('db', 'password')
        self.mysql=pymysql.connect(host=host, user=user, password=password, port=3306)
        self.cursor = self.mysql.cursor()
    def fetch_one(self,sql):  #查询数据库
         self.cursor.execute(sql)
         result=self.cursor.fetchone()

         return result

    def close_mysql(self):
        self.cursor.close()
        self.mysql.close()

if __name__ == '__main__':
         mysql=MysqlUntil()
         sql="select max(mobilephone) from future.member"
         res=mysql.fetch_one(sql)
         mysql.close_mysql()
         print(type(res))
         print((res))


# print(host)



