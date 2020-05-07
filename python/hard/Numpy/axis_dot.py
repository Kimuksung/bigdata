# -*- coding: utf-8 -*-
"""
1. 축(axis) : 행축 , 열축
2. 행렬 곱 연산 : np.dot()
    회귀방정식 = [X * a] + b
    X1 , X2 -> a1 , a2
    model = X1 * a1 + X2 *a2 + b
    model = np.dot(X,a) + b
    
    - 신경망에서 행렬곱 예
    [X * weight] + b

"""

import numpy as np

# axis
'''
행 축 : 동일한 열의 모음 (axis=0)
열 축 : 동일한 행의 모음 (axis=1)
'''

arr2d = np.random.randn(5,4)
arr2d

arr2d.sum(axis=0)
arr2d.sum(axis=1)

# 행렬 곱 연산 np.dot()
# 전제 조건
# 1) x,a 행렬 구조
# 2) 수일치
x= np.array([[2,3],[2.5,3]])
x
x.shape

a=np.array([[0.1],[0.05]]) #기울기
b= 0.1
y_pred = np.dot(x,a) + b 
y_pred
