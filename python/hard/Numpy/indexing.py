# -*- coding: utf-8 -*-
"""
indexing / slicing
    - 1 demension indexing : list 동일
    - 2,3 demension indexing
    - boolean indexing
"""

import numpy as np

# 1. indexing
'''
1d : obj[index]
2d : obj[row index , column index]
3d : obj[면 index , row index ,column index]
'''

# 1) list object
ldata = [0,1,2,3,4,5]
ldata[:] #all
ldata[2:] # [n:~]
ldata[:3]
ldata[-1]

# 2) numpy object
arr1d = np.array(ldata)
arr1d.shape
arr1d[2:]
arr1d[:3]
arr1d[-1]

# 2. slicing
arr = np.array(range(1,11))
arr # 원본

arr_sl = arr[4:8]
arr_sl # 사본

# 블럭 수정
arr_sl[:] = 50
arr_sl

arr #사본을 수정하게 되면 원본도 같이 수정된다.

# 2차, 3차 indexing
arr2d = np.array([[1,2,3],[2,3,4],[3,4,5]])
arr2d.shape

arr2d

# row index : default
arr2d[1]  #arr2d[1,:]
arr2d[:,1:]
arr2d[2,1]

arr2d[:2,1:]

# [면,행 열] : 면 index -> default
arr3d = np.array([ [[1,2,3],[2,3,4],[3,4,5] ],[ [2,3,4],[3,4,5],[6,7,8] ]])
arr3d

arr3d.shape #(2, 3, 3)
arr3d[0]
'''
array([[1, 2, 3],
       [2, 3, 4],
       [3, 4, 5]])
'''

# 면 -> 행 index
arr3d[0,2] # array([3, 4, 5])

# 면 -> 행 -> 열 index
arr3d[1,2,2] # 8 

arr3d[1,1:,1:]

# 3. boolean indexing
dataset = np.random.randint(1,10,size=100)
len(dataset)

dataset2 = dataset[dataset>=5]
len(dataset2)

# dataset2 = dataset[dataset>=5 and dataset<=8] 이런식으로는 불가 
np.logical_and()
np.logical_not()
np.logical_or()

dataset3 = dataset[np.logical_and(dataset>=5 , dataset<=8)]
dataset3







