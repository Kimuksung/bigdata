'''
Maria DB 연동 TEST
'''
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try:
    import pymysql

    #print(pymysql.version_info)
    conn = pymysql.connect(**config)

    cursor = conn.cursor()

    sql = "select * from goods"
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)

except Exception as e :
    print("error : ",e)
    conn.rollback()

finally:
    pass