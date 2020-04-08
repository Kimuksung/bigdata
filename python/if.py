'''
제어문 : 조건문 if , 반복문 while , for
python 블럭 : 콜론과 들여쓰기
'''

var = 10
if var>= 10:
    print("True")

var =2

if var >=5 :
    print("True")
else:
    print("False")

"""
temp = int(input())
if temp>=60:
    print("합격")
else:
    print("불합격")
"""
import datetime
today = datetime.datetime.now() #module.class.method()
print(today)

day = today.weekday()
print(day) # 0 ~ 4 : 월 ~ 금

if day>= 5:
    print("휴일")
else:
    print("평일")

# 블럭 if vs 라인 if
num = 9
if num >= 5 :
    result = num * 2
else:
    result = num + 2

print(result)
# 변수 = 참 if 조건문 else 거짓
result2 = num*2 if num >=5 else num+2
print(result2)


