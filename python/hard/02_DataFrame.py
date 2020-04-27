# -*- coding: utf-8 -*-
"""
DataFrame 자료 구조 특징
    - 2차원 행렬 구조(table 구조)
    - 열 단위 데이터 처리 용이
    - Series의 모음 -> Dataframe
"""

import pandas as pd

# 1. dataframe 생성

# 1) 기본 자료 구조(list , dict) 이용
name = ['kim','lee','hong','park'] 
age = [35 , 45 , 55 , 27]
pay = [600, 500,200 , 400]
addr = ['seoul', 'busan' , 'daejun' , 'bucheon']

data = {'name':name , 'age':age , 'pay':pay , 'addr' : addr}

df = pd.DataFrame(data = data , columns= ['name','age','addr','pay'])
print(df)

age = df['age'] #df.age
print(age.mean())

# 새 칼럼 추가
gender = pd.Series(['남','남','남','여'])
df['gender']  =  gender
print(df)

# 2) numpy 이용
import numpy as np
df2 = pd.DataFrame(np.arange(12).reshape(3,4),
                   columns = ['a','b','c','d'])
print(df2)

print(df2.mean(axis = 0)) #행축 : 열단위이다.
print(df2.mean(axis = 1)) #열축 : 행단위이다.

# 2) Dataframe column 참조
df2.index #행 이름
df2.values  # 값 이름

# emp.csv file load
emp = pd.read_csv("C:/ITWILL/4_Python-II/data/emp.csv" , encoding = 'utf-8')
print(emp.info())
print(emp.head())


# 단일 칼럼 선택
#emp['No']
#emp.No

# 복수 칼럼 선택 : 중첩 list
print(emp[['No','Pay']])
tmp = ['No','Pay']
print(emp[tmp])
