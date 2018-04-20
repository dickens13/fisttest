# import sys

import pymysql
# import redis


# def con_mysql(sql):
db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='123456',
        port=3306,
        db='0419',
        charset='utf8')
    # cursor = db.cursor()
    # cursor.execute(sql)
    # data = db.fetchall()
db.close()
#     return db

# def con_redis():
# 	r = redis.Redis(host='47.98.197.40', port=6379)

#     return r


# if __name__ == '__main__':
# 	# name = sys.argv[1]
# 	# passwd = sys.argv[2]
# 	print(con_redis())
