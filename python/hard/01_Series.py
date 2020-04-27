# -*- coding: utf-8 -*-
"""
series object
    - one darray
    - 수학 통계 함수 제공
    - 범위 수정, 블럭 연산
    - indexing , slicing
    - 시계열 데이터 생성
"""

import pandas as pd
from pandas import Series

# 1 . Series 객체 생성

# 1) list 이용
lst = [4000,3000,3500,2000]
ser = pd.Series(lst) # list -> Series

ser1_2 = Series([4000,3000,3500,2000] , index = ['a','b','c','d'])
print(ser1_2.index)
print(ser1_2.values)
print("-"*20)

# object.member
print(ser.index)
print(ser.values)

print("-"*20)
# 2) dictionary 이용
person ={'name': '홍길동' , 'age': 35 , 'addr':"seoul"}
ser2 = Series(person)
print(ser2)

print(ser2.index)
print(ser2.values)

# index 사용법
print(ser2['age'])
#object[ index or 조건식]

# 조건식
print(ser[ser>=3000])

# 2. indexing 설정 : list와 동일
#ser3 = Series()  생성자

ser3 =Series([4,4.5,6,8,10,5])
print(ser3[0])
print(ser3[:3])
# there is no minus index
# print(a[-1]) X


#3. Series 결합과 NA 처리
p1 = pd.Series([400,None,350,200],index=['a','b','c','d'])
p2 = Series([400,150,350,200],index=['a','c','b','e'])
p3 = p1+p2

print(p3)

# 4. 결측치 처리 방법(평균,0,제거)
# 평균 대체
p4 = p3.fillna(p3.mean())
print(p4)

p4 = p3.fillna(0)
print(p4)

p5 = p3[pd.notnull(p3)] #subset을 만들어라
print(p5)

print("*"*20)
# 5. 범위 수정 , 블럭 연산
print(p2)

p2[1:3] = 300
print(p2)

#list에서는 범위 수정이 불가능

#블럭연산
print(p2 + p2 )
print(p2 - p2)

#broadcast 연산(1차 vs 0차)
v1 = Series([1,2,3,4])
scala = 0.5
v2 = v1 *scala
print(v2)


# 수학 통계 함수
# v1.sum() / v1.mean() / v1.var() / v1.std() / v1.min() 

# 호출 가능한 멤버 확인
print(dir(v1))

print(v1.shape)
print(v1.size)
