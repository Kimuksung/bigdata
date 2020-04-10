'''

1. 축약 함수(lambda)
- 한줄 함수
형식) value = lambda 인수 : return

ex) lambda x,y : x+y
'''

# 1. 축약 함수
def adder(x,y):
    return x+y

add = lambda x,y : x+y
print(add(10,20))
#[lambda for 변수 in 열거형 객체]

# 2. scope
# - 전역변수, 지역변수
x=50
def local_func(x):
    x+= 50

def global_func():
    global x
    x+=50

local_func(x)
print(x)
global_func()
print(x)