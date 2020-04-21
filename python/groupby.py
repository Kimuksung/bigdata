'''
group by 집단 변수(범주형)

'''

import pymysql
import sys
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    gcol = int(sys.stdin.readline().strip())
    if gcol ==1:
        sql = "select dno , sum(sal) , round(avg(sal),2) from emp group by emp.dno order by dno"
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in data:
            print(i)
    elif gcol ==2:
        sql = "select job, sum(sal) , round(avg(sal),2) from emp group by emp.job order by job"
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in data:
            print(i)
    else:
        print("wrong input data")
except Exception as e:
    print(e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()