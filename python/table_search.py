'''
table 전체 조회 -> 생성 및 조회
1. 없는 경우 : table 생성
2. 있는 경우 : table 조회
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

    #1. 전체 table 조회
    cursor.execute("show tables")
    tables = cursor.fetchall()

    #table 유무 검색
    sw = False
    if tables:
        for t in tables:
            #print(t[0])
            if t[0] == 'emp':
                sw = True

    if sw == False: #table 생성 -> record 삽입
        print("emp_table is not exist")
        sql = """create table emp(
            eno int auto_increment primary key,
            ename varchar(20) not null,
            hiredate date not null,
            sal int,
            bonus int default 0,
            job varchar(20) not null,
            dno int
        )
        """
        cursor.execute(sql) #table 생성
        sql2 = "alter table emp auto_increment = 1001"
        cursor.execute(sql2)

        sql3 = "insert into emp(ename,hiredate,sal,bonus,job,dno) values('kimuksung','2013-07-21',6000000,2000000,'관리자',10)"
        cursor.execute(sql3)
        sql3 = "insert into emp(ename,hiredate,sal,bonus,job,dno) values('kimnamjun','2014-09-21',4000000,200000,'사원',8)"
        cursor.execute(sql3)
        sql3 = "insert into emp(ename,hiredate,sal,bonus,job,dno) values('ParkJ','2020-05-21',3000000,100000,'사원',10)"
        cursor.execute(sql3)
        conn.commit()

        print("table complete")

    else: #record 조회
        #print("emp_table exist")

        sql = "select * from emp"
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in data:
            print(i)
        '''
        #사원 조회
        job = sys.stdin.readline().strip()
        sql =f"select eno,ename,dno from emp where job like '%{job}%'"
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in data:
            print(i)
        
        # 사번 급여 보너스 -> 급여 , 보너스 수정
        eno = sys.stdin.readline().strip()
        sal = sys.stdin.readline().strip()
        bonus = sys.stdin.readline().strip()
        sql =f"update emp set sal={sal} , bonus={bonus} where eno={eno}"
        cursor.execute(sql)
        conn.commit()
        

        eno = sys.stdin.readline().strip()
        sql = f"select * from emp where eno = {eno}"
        cursor.execute(sql)
        data=cursor.fetchall()
        if data:
            sql = f"delete from emp where eno={eno}"
            cursor.execute(sql)
            conn.commit()

            print("Delete Complete")
        else:
            print("There is no data for delete")

        sql = "select * from emp"
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in data:
            print(i)
'''
except Exception as e:
    print(e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()