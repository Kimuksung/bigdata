# -*- coding: utf-8 -*-
"""
Numpy package 특징
    - 선형 대수(벡터, 행렬) 연산 관련 함수 제공
    - list 보다 이점 : N차원 배열 생성, 선형 대수 연산 , 고속 처리
    - Series 공통점
        -> 수학 통계 함수 지원 obj.sum() ..
        -> 범위 수정 , 블럭 연산
        -> indexing / slicing
    
    - 주요 모듈 / 함수
        1. random
        2. array : N 차원 배열 생성 array([[list]])
        3. sampling 함수
        4. arrange : range() 유사함 
        
    - 차이점
    
"""

import numpy as np

lst = [1,2,3]

#lst **2 # TypeError

for i in lst:
    print(i**2)
    
# list -> numpy
arr = np.array(lst)

arr #array([1, 2, 3])
arr**2 #array([1, 4, 9], dtype=int32)


#same type -> 1(str)
arr=np.array([1,'two',3])
arr #array(['1', 'two', '3'], dtype='<U11')

arr=np.array([[1,'two',3]])
arr #array([['1', 'two', '3']], dtype='<U11')
arr.shape #(1, 3)

# 1. random 
data = np.random.randn(3,4) #module.module.function()
data
'''
array([[ 0.09221763, -0.73739475,  1.27512942,  0.94264521],
       [ 0.10630184,  0.56524047, -0.32904701, -1.85714391],
       [-0.36193492,  2.21153018, -0.16136962,  0.2817693 ]])
'''

for row in data:
    print(row.sum())
    print(row.mean())
    
# 1) 수학 통계 함수 지원
type(data)
print("전체 합계:",data.sum())
print("전체 평균:",data.mean())
print("전체 분산:",data.var())
print("전체 표준편차:",data.std())    

dir(data)
data.shape
data.size

# 2) 범위 수정, 블럭 연산
data + data
data - data

# 3) indexing
data[0,0] # 1행 1열 
data[0,:] # 1행 전체
data[:,1] # 2열 전체

# 2. array 함수 : N 차원 배열 생성
# List는 수학 통계 function X But numpy는 가능

# 1) 단일 List
lst1 = [3,5.6,4,7,8]
# list -> array
arr1 = np.array(lst1)
arr1

arr1.var()

# 2) 중첩 List
lst2 = [[1,2,3,4,5],[2,3,4,5,6]]
lst2
lst2[0][2] #3

arr2 = np.array(lst2)
arr2
'''
array([[1, 2, 3, 4, 5],
       [2, 3, 4, 5, 6]])
'''

arr2.shape
arr2[0,2] #3
arr2[1,:] # 2 row all array([2, 3, 4, 5, 6])
arr2[:,1] # 2열 전체 : [2,3] 
arr2[:,2:4]
'''
array([[3, 4],
       [4, 5]])
'''

# broadcast 연산
# - 작은 차원이 큰 차원이 늘어난 뒤 연산

# scala(0d) vs vector(1d)
0.5 * arr1 # array([1.5, 2.8, 2. , 3.5, 4. ])

# scala(0d) vs matrix(2d)
0.5 * arr2
'''
array([[0.5, 1. , 1.5, 2. , 2.5],
       [1. , 1.5, 2. , 2.5, 3. ]])
'''

# vector(1d) vs matrix(2d)
print(arr1.shape , arr2.shape)

arr3 = arr1 + arr2
print(arr3)
'''
[[ 4.   7.6  7.  11.  13. ]
 [ 5.   8.6  8.  12.  14. ]]
'''

# 3. sampling function
num = list(range(1,11))
num
'''
a : 관측치 길이
size : 임의 추출 크기
replace : 복원 or 비복원
p : 확률
'''
idx = np.random.choice(a=len(num),size = 5 , replace=False) #module.module.function
idx #array([0, 8, 1, 5, 6])

import pandas as pd

score = pd.read_csv("score_iq.csv")
score 
len(score) # 150
idx = np.random.choice(a=len(score),size = int(len(score)*0.3) , replace=False)
idx

# dataframe indexing
score_train = score.iloc[idx,:]
score_train.shape #(45, 6)

# pandas -> numpy
score_arr = np.array(score)
score_arr.shape #(150, 6)
score_train2 = score_arr[idx,:]
score_train2.shape #(45, 6)


# 4. arrange function
zero_arr = np.zeros((3,5))
zero_arr
'''
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
'''
cnt = 1
for i in range(3): #행index
    for j in range(5): #열 index
        zero_arr[i,j] = cnt
        cnt+=1
        
zero_arr

#range (-1.0 , 2,0.1) #type error
np.arange(-1.0 , 2,0.1)
























