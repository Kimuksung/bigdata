'''
method override
- 부모의 원형 메소드 -> 자식에 원형 메서드를 다시 작성하는 문법
- 상속관계에서만 나오는 용어
- 인수, 내용 -> 수정 대상

다형성
- 상속 관계 용어
- 한 가지 기능 -> 2개 이상 결과 생성
- 부모 object -> 자식 멤버 호출
'''

#1 . 메서도 재정의

class Parent :
    data = None

    def superFunc(self):
        pass

class Sub1(Parent):

    def superFunc(self,data): # method override
        self.data = data
        print(self.data)

import datetime
tmp = Sub1()
tmp.superFunc(datetime.datetime.now())
#print(tmp.data)

class Sub2(Parent):
    def superFunc(self,data):
        self.data = data
        print("this is Sub2 function data : ",self.data)

tmp1 = Sub2()
tmp1.superFunc(100)


# 다형성
p1 = Parent()
sub1 = Sub1()
sub2 = Sub2()

p1 = sub1
p1.superFunc("hi")
