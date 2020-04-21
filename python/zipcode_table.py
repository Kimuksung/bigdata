'''
줄단위 text -> table
text file -> DB save

<작업 순서>
1. table 생성
2. zipcode.txt -> readlines -> record save
3. table 저장 -> 검색

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

    # table 생성
    '''
    sql = """create or replace table zipcode_tab
    (
        code char(14) not null , 
        city char(20) not null , 
        gu varchar(20) not null , 
        dong varchar(80) not null,
        detail varchar(50)
    )"""
    cursor.execute(sql)
    print("table complete")
    '''

    #record 조회
    sql = "select * from zipcode_tab"
    cursor.execute(sql)
    data = cursor.fetchall()

    if data: #검색
        '''
        for row in data:
            print("[%s] %s  %s  %s  %s"%row)
        
        print(len(data))

        # 동 검색
        dong = sys.stdin.readline().strip()
        cursor.execute(f"select * from zipcode_tab where dong like '%{dong}%'")
        data = cursor.fetchall()
        for row in data:
            print(row)
        '''
        #구 검색
        gu = sys.stdin.readline().strip()
        cursor.execute(f"select * from zipcode_tab where gu like '%{gu}%'")
        data = cursor.fetchall()
        for row in data:
            print(row)
    else:
        file = open("../data/zipcode.txt" ,encoding="utf-8")
        line =file.readline()

        while(line):
            row = line.split("\t")
            if row[1] == '서울':
                code = row[0]
                city = row[1]
                gu = row[2]
                dong = row[3]
                detail = row[4]

                if detail:
                    sql=f"insert into zipcode_tab values('{code}','{city}','{gu}','{dong}','{detail}')"

                else:
                    sql = f"insert into zipcode_tab (code,city,gu,dong) values('{code}','{city}','{gu}','{dong}')"

                cursor.execute(sql)
                conn.commit()
            line = file.readline()
        file.close()
        print("record add complete")


except Exception as e:
    print("error : " ,e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()