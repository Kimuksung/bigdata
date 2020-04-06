'''
변수(Variable)
- 변수명 = 값 or 수식 or 변수명
- 자료를 저장하는 메모리 이름
- type을 따로 지정하지 않는다.
'''

# 1. 변수와 자료
var1 = "Hello python"
var2 = 'Hello python'

print(var1)
print(var2)
print(type(var1))

var1 = 100
print(var1, type(var1))

var2 = 150.25
print(var2 , type(var2))

var3 =True
print(var3 , type(var3))

_num10 = 10
_NUM10 = 20
print(_num10,_NUM10)
print(id(_num10), id(_NUM10))

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

# 참조 변수 : 메모리 객체(value)를 참조하는 주소 저장 변수
x = 150 #150의 object address
y = 45.23
y2 = y #변수 복제
x2= 150 # 기존 객체 있으면 ,주소 반환

print(x,y,y2,x2)
print(id(x),id(y),id(y2),id(x2))