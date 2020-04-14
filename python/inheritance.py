'''
클래스 상속(Inheritance)

- 기존 클래스(부모)를 이용하여 새로운 클래스 생성 문법
- 부모 클래스 정의 -> 자식 클래스 생성
- 상속 대상 : 멤버(o) + 생성자(x)
    -> 생성자 상속 대상 아님

class 자식class(부모class):
    멤버
    생성자



'''

# 부모 클래스
class Super :
    # 멤버 변수
    name = None
    age = 0

    # 생성자 : 객체 생성 + 초기화
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 멤버 메서드 : 데이터 처리
    def display(self):
        print(self.name , self.age)

super = Super("부모",55)
super.display()

# 자식 class
class Sub(Super):
    num=""
    gender = ""
    def __init__(self,name,age,num,gender):
        Super.__init__(self,name,age)
        self.num = num
        self.gender = gender

    def display(self):
        print(self.name , self.age,self.num , self.gender)


sub = Sub("uksung",27,"01043939492","man")
sub.display()

class Parent :
    name = job = None
    def __init__(self,name,job):
        self.name = name
        self.job = job

    def display(self):
        print(self.name , self.job)

p1 = Parent('kimuksung','engineer')
p1.display()

class Children1(Parent):
    gender = None
    def __init__(self,name,job,gender):
        Parent.__init__(self,name,job)
        self.gender = gender
    def display(self):
        print(self.name, self.job, self.gender)

p2 = Children1("kimuksung","engineer","man")
p2.display()

