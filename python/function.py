'''
함수의 가변 인수
- 한개의 가인수로 여러개의 실인수를 받는 인수
 def function(*value)
 *value -> 가변 인수

'''

# 1. tuple 형으로 받는 가변 인수
def fun1(name,*names):
    print(name)
    print(names)
    print(type(names))
fun1('홍길동','이순신','유관순')

# package , module
import scatter.scatter_module
from scatter.scatter_module import Avg,var_std
# from package.module import function,class
datas=[2,3,5,6,7]
print(scatter.scatter_module.var_std(datas))

print(var_std(datas))

def statis( func , *data):
    if func == 'sum' :
        return sum(data)
    elif func =='avg':
        return Avg(data)
    elif func == 'var':
        return var_std(data)
    elif func =='std':
        return var_std(data)
    else:
        return "no function right that"

print(statis('sum',1,2,3,4,5))

# 2. dict 형 가변인수
def person(w,h, **other ) :
    print('w=' , w)
    print('h=',h)
    print(other)

person(65, 175, name = '홍길동',age=15)

# 3. 함수를 인자로 받기
def square( x ):
    return x**2

def my_func(func , datas):
    result = [ func(d) for d in datas]
    return result

print(my_func(square,datas))