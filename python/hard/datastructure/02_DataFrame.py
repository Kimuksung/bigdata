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
'''
print(emp.info())
print(emp.head())


# 단일 칼럼 선택
#emp['No']
#emp.No

# 복수 칼럼 선택 : 중첩 list
print(emp[['No','Pay']])
tmp = ['No','Pay']
print(emp[tmp])

import matplotlib
no = emp.No
no.plot()
pay = emp['Pay']
pay.plot()
tmp = emp[['No','Pay']]
tmp.plot()
'''

# 3. subset 만들기 : old DF -> new DF

# 1) 특정 칼럼 제외 : 칼럼이 적은 경우

print(emp.info())
subset1 = emp[['Name','Pay']]
subset1

# 2) 특정 행 제외
subset2 = emp.drop(0)
subset2

# 3) 조건식으로 행 선택
subset3 = emp[emp.Pay > 350]
subset3

# 4) columns 이용 : 칼럼 많은 경우
iris = pd.read_csv("C:\\ITWILL\\4_Python-II\\data/iris.csv" , encoding = "utf-8")
iris.info()
iris.head()

iris['Sepal.Length']

cols = list(iris.columns)
cols
type(cols)

iris_x = cols[:4]
iris_y = cols[-1]
iris_x
iris_y

x = iris[iris_x]
y = iris[iris_y]
x.shape
y.shape

# 4. DataFrame 행렬 참조 DF[row,col]
# 1) DF.loc[row,col] : label index
# 2) DF.iloc[row,col] : integer index

emp.loc[1:3 , :]
emp.loc[:, 'No':'Name']
emp.loc[:, ['No','Pay']]

emp.iloc[1:3]
emp.iloc[1:3 , 0:2]
emp.iloc[1:3 , [0,2]]

####################
# df 행렬 참조
####################
iris.shape

from numpy.random import choice
row_idx = choice(a= len(iris) ,size = int(len(iris)*0.7),replace=False)
row_idx

train_set = iris.iloc[row_idx]
train_set

train_set2 = iris.loc[row_idx]
train_set2

test_idx = [i for i in range(len(iris)) if not i in row_idx]
test_set = iris.iloc[test_idx]
test_set.shape

# x,y 분리
cols = list(iris.columns)
x = cols[:4]
y = cols[-5]
iris_x = iris.loc[test_idx, x]
iris_y = iris.loc[test_idx,y]
iris_x
iris_y
