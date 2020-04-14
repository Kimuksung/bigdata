'''
1. privat 변수 = 클래스 내의 은닉 변수
    object.member : 객체를 토대로 은닉변수로 접근하게 되면 접근 불가
    -> get set func 을 이용

2. class 포함 관계(inclusion)
- 특정 개체가 다른 객체를 포함하는 클래스 설계 기법
- 두 객체 간의 통신 지원
class A(a) <-> class B(b)
'''

# 1. private 변수
class Login :
    def __init__(self, id, pw):
        self.__dbid = id
        self.__dbpw = pw

    def get(self):
        return self.__dbid,self.__dbpw

    def set(self,id,pw):
        self.__dbid = id
        self.__dbpw = pw


user = Login("kimuksung2","ww0603")
print(user.get())
user.set("kimuksung2","123456")
print(user.get())

# Server <-> Login
class Server:
    def send(self,obj): # object 인수로 받음
        self.obj = obj # 멤버 변수 생성

    #인증 메소드
    def cert(self , id , pw):
        dbId , dbpw = self.obj.get()
        if dbId == id and dbpw ==pw :
            print("Login success")
        else:
            print("Login failed")

nodejs = Server()
nodejs.send(user)
nodejs.cert("kimuksung2","123456")