'''
emp join dept
subquery : dept , emp
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
    '''
    sal = int(sys.stdin.readline().strip())
    #inner join
    sql = f"select e.eno,e.ename , e.sal,d.dname from emp e inner join dept d on e.dno=d.dno and e.sal >= {sal}"
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)
    
    # subquery : 부서번호(dept) -> 사원
    dno = int(sys.stdin.readline().strip())
    sql = f"""
        select eno , ename , hiredate , dno from emp 
        where dno = (select dno from dept where dno = {dno}
        )
    """
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)
    '''
    ename = sys.stdin.readline().strip()
    sql = f"select * from dept where dno = (select dno from emp where ename ='{ename}')"

    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print(i)

except Exception as e:
    print(e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()