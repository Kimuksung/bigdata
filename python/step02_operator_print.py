'''
연산자 (operator)
1. 변수에 값 할당(=)
2. 연산자 : 산술 , 관계 ,논리
3. print 형식
4. input : 키보드 입력
'''

#1. 변수에 값 할당
i= tot = 10
i += 1
i += 1
tot +=1
print(id(i))
print(id(tot))

v1, v2 = 100,200
v1 , v2 = v2,v1
print(v1,v2)

# packing
lst = [1,2,3,4,5]
v1,*v2 = lst
print(v1,v2)

*v1 ,v2 = lst
print(v1,v2)

#2. 연산자 : 산술 관계 논리
num1 = 100 #피연산자1
num2 = 20.5 #피연산자2

add=num1+num2
div = num1/num2
div2 = num1 //num2
div3 = num1 % num2
square = num1**2
print(div)
print(div2)
print(div3)
print(square)


lst = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7]
]

for i in lst:
    a , *b = i
    print(a,b)

# 논리 연산자 or , and , not
print(9>10 or 11>10)
print(9>10 and 11>10)
print(not(9>10) and 11>10)

# print 형식
help(print) # 함수 도움말
print( end="\n")

# format(value , '형식')
print("원주율=", format(3.14159, "8.3f") ) # 원주율= 3.142
print("금액 =", format(10000, "10d")) # 금액 = 10000
print("금액 =", format(125000, "3,d")) # 금액 = 125,000

#% print("양식문자" %(값))
print( "%d + %d = %d" %(num1,num2,add))
print("8진수 = %o , 16진수 = %x" %(num1,num1))

print("%s = %8.3f" %("PI",3.14159))

# 외부 상수 받기
# "{},{}".format(value1,value2,..)
print("name : {} , age : {}".format("홍길동",35))
print("name : {1} , age : {0}".format("홍길동",35)) #name : 35 , age : 홍길동

# 4. input("prompt")
#a = input()
#b = input()

a,b = map(float , input().strip().split())
print(a,b)