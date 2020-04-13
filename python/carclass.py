'''

동적 멤버 변수 생성
 - 필요한 경우 특정 함수에서 멤버 변수 생성
 self : class의 멤버를 호출 하는 역할 self.member / self.method()
'''

class Car:
    door = cc = 0
    name = None # null

    #생성자 : 객체 + 초기화
    def __init__(self , door , cc , name):
        self.door = door
        self.cc= cc
        self.name = name

    def info(self):
        self.kind = ""
        if self.cc>=3000:
            self.kind = "대형"
        else:
            self.kind="소형"
        self.display()

    def display(self):
        print( self.name , self.cc,self.door)

tmp1 = Car(2,4000,'uk')
print(tmp1.info())
#print(tmp1.kind)
tmp2 = Car(4,3000,'GRAMDer')
print(tmp2.info())