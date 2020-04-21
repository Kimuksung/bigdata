'''
CRUD
    create , read , update , delete

'''

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

import pymysql
import sys

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    '''
    #insert
    code = int(sys.stdin.readline())
    name = sys.stdin.readline().strip()
    su = int(sys.stdin.readline())
    dan = int(sys.stdin.readline())
    sql = f"insert into goods values ({code},'{name}',{su},{dan})"
    cursor.execute(sql)
    conn.commit()
    

    #update
    code = int(sys.stdin.readline())
    su = int(sys.stdin.readline())
    dan = int(sys.stdin.readline())
    sql = f"update goods set su ={su}, dan={dan} where code={code}"
    cursor.execute(sql)
    conn.commit()
    

    # delete : code -> 유무 -> 삭제 or '코드 없음'
    code = int(sys.stdin.readline().strip())
    cursor.execute(f"select * from goods where code ={code}")
    data = cursor.fetchone()
    if data:
        cursor.execute(f"delete from goods where code ={code}")
    else:
        print("There is no Data")
    conn.commit()
    '''
    # read
    sql = "select * from goods"
    cursor.execute(sql)
    data = cursor.fetchall()

    for i in data:
        print(i)

    print('전체 레코드 수:',len(data))
    '''
    # 상품명 조회
    name = input("name :")
    sql = f"select * from goods where name like '%{name}%'"
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        for i in data:
            print(i)
    else:
        print("There is no data")

    conn.commit()
    
    # 상품 코드
    #code = int(input("조회 상품명 입력 : "))
    code=int(sys.stdin.readline())
    sql = f"select * from goods where code = {code}"
    cursor.execute(sql)
    data = cursor.fetchall()
    if data:
        for i in data:
            print(i)
    else:
        print("There is no data")
    '''
except Exception as e:
    print("Error :", e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()