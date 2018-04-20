# -*- coding:utf8 -*-
import pymysql

# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect(host='10.7.189.59',
                     user='root',
                     password='123456',
                     database='test',
                     port=3306,
                     charset='utf8')
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * from my")
date = cursor.fetchall()
for i in date:
    print(i)
# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
# print("Database version : %s " % data)

# 关闭数据库连接
db.close()