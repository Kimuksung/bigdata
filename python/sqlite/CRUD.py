'''
CRUD
    -create
    -read
    -update
    -delete

'''

import sqlite3


try:
    # database 생성
    conn = sqlite3.connect("../data/sqlite.db")
    # sql문 실행 객체
    c = conn.cursor()

    sql = """create table if not exists goods 
    (
    code integer primary key , 
    name text(30) unique not null , 
    su integer default 0,
    dan real default 0.0
    )
    """
    '''
    c.execute(sql)

    c.execute("""insert into goods values (1, '냉장고' , 2 , 850000)""")
    c.execute("""insert into goods values (2, '세탁기' , 5 , 550000)""")
    c.execute("""insert into goods(code , name) values (3, '전자레인지')""")
    c.execute("""insert into goods(code , name, dan) values (4, 'TV' , 1500000 )""")

    conn.commit()
    '''
    code = int(input('code'))
    name = input('name')
    su = int(input('su'))
    dan = int(input('dan'))
    sql = f"insert into goods values ({code},'{name}',{su},{dan})"
    c.execute(sql)
    conn.commit()

    '''
    # update record
    sql = "update goods set name='테스트' where code = 4"
    c.execute(sql)
    conn.commit()

    code = int(input("code :"))
    su = int(input("su :"))
    dan = int(input("dan :"))
    
    sql = f"update goods set dan={dan} , su={su} where code = {code}"
    c.execute(sql)
    conn.commit()
    
    code = int(input("delete code :"))
    sql = f"select * from goods where code = {code}"
    c.execute(sql)
    data = c.fetchall()
    print(data)
    if data:
        sql = f"delete from goods where code = {code}"
        c.execute(sql)
        conn.commit()
        print("delete complete")
    else:
        print("no code data")
    '''
    c.execute("""select * from goods""")
    data = c.fetchall()
    for i in data:
        print("%d   %s  %d  %d"%(i))
    print("data num : " , len(data))
    '''
    c.execute("""select * from goods where su>=2""")
    data = c.fetchall()

    for i in data:
        print("%d   %s  %d  %d"%(i))
    print("data num : " , len(data))
    
    name = input("goods :")
    c.execute(f"""select * from goods where name like '%{name}%'""")
    #c.execute(f"""select * from goods where name like {name}""")
    data = c.fetchall()

    if data:
        for i in data:
            print("%d   %s  %d  %d"%(i))

    else:
        print("no searching data")
    '''



except Exception as e :
    print("database error :" , e)
    conn.rollback()

finally:
    c.close()
    conn.close()

