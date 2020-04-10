'''
중첩 함수(inner function)

형식)
def outer_func(인수) :
    실행문
    def inner_func(인수):
        실행문
    return inner_func
'''

# 1. 중첩함수 예
def a(): #outer
    print('afunction')

    def b():
        print('bfunction')

    return b

b = a() #outer 호출  -  일급 함수(inner 함수가 객체로 나타난다)
'''
for i in range(0,10):
    b()
'''
# 2. 중첩 함수 응용
'''
getter() : 함수 내의 data를 외부 획득자
setter() : 함수 내의 data를 handling
'''

def outer_funct(data):
    dataset = data # 데이터 저장 , inner 포함
    def tot():
        tot_value = sum(dataset)
        return tot_value

    def avg(tot_value):
        avg_value = tot_value / len(dataset)
        return avg_value
    def getData():
        return dataset

    def setData(newData):
        nonlocal dataset
        dataset= newData

    return tot,avg,getData,setData

data = list(range(1,101))
'''
tot , avg ,getData , setData= outer_funct(data)
tot_val = tot()
print(tot_val) #합계 계산
print(avg(tot_val)) # 평균 계산
print(getData())

new_data = list(range(1,5))
setData(new_data)
print(getData())

def bank_account(balance):
    money = balance
    def getBalance():
        return money
    def deposit(add):
        nonlocal money
        money += add
    def widthdraw(minus):
        nonlocal  money
        if money < minus:
            print("잔액이 부족합니다")
        else:
            money-= minus
    return getBalance , deposit , widthdraw

balance = int(input("balance:"))

getBalance , deposit , widthdraw = bank_account(balance)
print( "현재 잔액 : ", getBalance())
add = int(input("deposit:"))
deposit(add)
print( "현재 잔액 : ", getBalance())
minus = int(input("widthdraw:"))
widthdraw(minus)
print( "현재 잔액 : ", getBalance())

'''
'''
 3. 함수 장식자 : Tensorflow2.0
 - 기존 함수의 시작 부분과 종료 부분의 기능 추가해서 장식
 
@함수 장식자
# def function():
    실행문
'''

#함수 장식자 선언
def hello_deco(func): # outer 함수를 인수로 받는 역할
    def inner(name) : #함수 장식 하는 역할 target의 parameter도 받는 역할
        print('-'*20)
        func(name)
        print('-'*20)
    return inner

@hello_deco
def hello(name):
    print("my name is "+name)

hello("kim uk sung")
hello("park")

#구구단 장식

def deco(func):
    def inner(num):
        print("*" *20)
        func(num)
        print("*"*20)
    return inner

@deco
def gugu(i):
    for j in range(1,10):
        print(f"{i}*{j} = {i*j}")

while True:
    num = int(input())
    gugu(num)


