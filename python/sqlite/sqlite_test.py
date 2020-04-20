'''
sqllite3
    - 내장형 DBMS
    - 외부 접근 허용 X
    -

'''

import sqlite3

print(sqlite3.sqlite_version_info)

try:
    #database 생성
    conn = sqlite3.connect("../data/sqlite.db")
    #sql문 실행 객체
    c = conn.cursor()
    sql = """CREATE TABLE if not exists test_tab(name text(10) , phone text(15), addr text(50) )"""
    c.execute(sql) # table 생성

    #record insert
    '''
    sql = """INSERT INTO test_tab values ('kimuksung', '010-4393-9492', 'seoul' )"""
    c.execute(sql)
    sql = """INSERT INTO test_tab values ('kimnam', '010-1234-5678', 'seoul' )"""
    c.execute(sql)
    sql = """INSERT INTO test_tab values ('parkJ', '010-4321-9494', 'bucheon' )"""
    c.execute(sql)
    conn.commit() # db 반영
    '''
    #record select
    c.execute("""select * from test_tab""")
    dataset = c.fetchall() # 객체 레코드 가져오기

    for row in dataset:
        print(row)

except Exception as e:
    print("Database error : ", e)
    conn.rollback() # error 발생 시 이전 상태로 되돌아간다.
finally:
    c.close()
    conn.close()

