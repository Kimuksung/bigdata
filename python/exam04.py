'''
문제4) emp.csv 파일을 읽어서 다음과 같이 db 테이블에 저장하시오.
 <조건1> 테이블명 : emp_table
 <조건2> 사원 이름으로 레코드 조회(sql문 작성)
 
 <작업순서>
 1. table 생성 : emp_table(sql 폴더)
 2. python code : 레코드 추가 
 3. python code : 레코드 조회(사원이름)  
'''

import pandas as pd 
import sys
# 칼럼 단위 읽기 
emp = pd.read_csv("../data/emp.csv", encoding='utf-8')
#print(emp)
# No Name  Pay
no = emp.No
name = emp.Name
pay = emp.Pay
print(no, name, pay)

import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try:

    conn =pymysql.connect(**config)
    cursor = conn.cursor()
    sql = """create or replace table emp_table
    (
        No int primary key , 
        Name char(10) not null , 
        Pay int not null  
    )"""

    cursor.execute(sql)
    for i in range(len(no)):
        sql = f"insert into emp_table values({no[i]},'{name[i]}',{pay[i]})"
        cursor.execute(sql)
    conn.commit()

    sql = "select * from emp_table"
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)

    print("-"*30)
    name = sys.stdin.readline().strip()
    sql = f"select * from emp_table where Name like '%{name}%'"
    cursor.execute(sql)
    data=cursor.fetchone()
    print(data)

except Exception as e:
    print(e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
