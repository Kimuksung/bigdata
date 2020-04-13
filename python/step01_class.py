'''
클래스(class)
-  object 생성 (multiple function and data share)
- 구성 요소 : 멤버(member) + 생성자
- 멤버(member) : 변수(자료 저장) + 메소드(자료 처리)
- 생성자 : 객체 생성
- 유형 : 사용자 정의 클래스 , 라이브러리 클래스(python)
형식)
class name:
    멤버 변수 = 자료
    멤버 메서드 = 자료 처리
    생성자 : 객체 생성

'''

# 1. 중첩 함수
def  calc_func(a,b):
    x=a
    y=b
    def plus():
        return x+y

    def minus():
        return x-y

    return plus,minus

p,m = calc_func(10,20) # 일급함수
print(p())
print(m())

# 2. class
class cal_class:
    # 멤버 변수 : 자료 저장
    x = y = 0
    # 생성자 : 객체 생성 + 멤버 변수 값 초기화
    def __init__(self,a,b):
        # 멤버 변수 초기화
        self.x=a
        self.y=b

    # 멤버 메서드 : 클래스에서 정의한 함수
    def plus(self):
        return self.x+self.y
    def minus(self):
        return self.x-self.y

tmp = cal_class(10,20)
print(tmp)
print(tmp.plus())
print(tmp.x)

tmp2 = cal_class(tmp.plus(),50)
print(tmp2.plus())

# 3. 라이브러리 클래스
from datetime import date

today = date(2020,4,13) # 생성자
print(today)

# object.member
print(today.year)
print(today.month)

week = today.weekday()
print(week)

