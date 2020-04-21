'''
문제3) 다음과 같은 메뉴를 이용하여 goods 테이블을 관리하시오.
    [레코드 처리 메뉴 ]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력 : 
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
    # db 연결 객체 생성 
    conn = pymysql.connect(**config)
    # SQL 실행 객체 생성 
    cursor = conn.cursor()    
    
    while True :  # 무한루프 
        print('\t[레코드 처리 메뉴 ]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')    
        menu = int(input('\t메뉴번호 입력 : '))
        
        if menu == 1 :
            sql = "select * from goods" # 1. 레코드 조회
            cursor.execute(sql)
            data = cursor.fetchall()
            for i in data:
                print(i)
        elif menu == 2:
            code = int(sys.stdin.readline())
            name = sys.stdin.readline().strip()
            su = int(sys.stdin.readline())
            dan = int(sys.stdin.readline())
            sql = f"insert into goods values ({code},'{name}',{su},{dan})"
            cursor.execute(sql)
            conn.commit()
        elif menu == 3:
            code = int(sys.stdin.readline())
            su = int(sys.stdin.readline())
            dan = int(sys.stdin.readline())
            sql = f"update goods set su ={su}, dan={dan} where code={code}"
            cursor.execute(sql)
            conn.commit()       # 3. 레코드 수정
        elif menu == 4:
            # 4. 레코드 삭제
            code = int(sys.stdin.readline().strip())
            cursor.execute(f"select * from goods where code ={code}")
            data = cursor.fetchone()
            if data:
                cursor.execute(f"delete from goods where code ={code}")
            else:
                print("There is no Data")
            conn.commit()
        elif menu == 5 :
            print('프로그램 종료')
            break # 반복 exit
        else :
            print('해당 메뉴는 없습니다.')
        
# DB 연결 예외 처리          
except Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close() 
