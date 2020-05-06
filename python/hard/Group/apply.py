# -*- coding: utf-8 -*-
"""
1. group object external function : apply
    - obj.apply()
    - obj.agg([func1 , func2, ... ])
    
2. data normalization

"""

import pandas as pd

# group object external function : apply
'''
apply vs agg
    - 공통점 : 그룹 object에 외부 함수 적용
    - 차이점 : 적용할 함수의 갯수
    
'''

test = pd.read_csv("test.csv")
test.info()

grp = test['data2'].groupby(test['key'])
grp.size()

# 사용자 정의 함수
def diff(grp):
    result=grp.max() - grp.min()
    return result

# 내장 함수 적용
print("-"*20)
grp.apply(sum)
grp.apply(max)
grp.apply(min)

print(grp.apply(diff))


# agg([func1,func2,func3,func4])

agg_func = grp.agg(['sum' , 'max' , 'min' , diff])
agg_func

# 2. data normalization : 다양한 특징을 갖는 변수를 대상으로 일정한 범위로 조정
import numpy as np # max , min , log

# 1) 사용자 정의 함수 : 0 ~ 1
def normal(x):
    n = (x-np.min(x)) / (np.max(x) - np.min(x))
    return n 


x = [10,20000,-100,0]

normal(x)

# 2) 자연 log
np.log(x) #밑 수 2
e  = np.exe(1)


# log -> 지수값
np.log(10)

# 지수 -> 로그
np.exp(2.302585092994)

'''
로그 vs 지수 역함수 관계
    - 로그 :지수값 반환
    - 지수:로그값 반환
    
'''

iris = pd.read_csv("iris.csv")

cols = list(iris.columns)

iris_x = iris[cols[:4]]
iris_x.info()
iris_x.shape
iris_x.head()

# x변수 normalization
iris_x_nor = iris_x.apply(normal)
iris_x_nor.head()

iris_x.agg(['var','mean','max','min'])

iris_y = iris[cols[-1]]


