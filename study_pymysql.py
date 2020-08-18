import pymysql
host='test.lemonban.com'
user="test"
password="test"
#test11111111111
#先自行安装这个模块  pip install pymysql
#1、建立连接
mysql=pymysql.connect(host,user, password, port=3306)
#2、新建一个查询页面
cursor=mysql.cursor()
#3、编写sql
sql='select max(mobilephone) from future.member'
#4、执行sql
cursor.execute(sql)
#5、查询结果
result=cursor.fetchone()
print(result[0])
#关闭查询
cursor.close()
#关闭数据库
mysql.close()
