# -*- coding: utf-8 -*-
"""
data scaling ( normalize , standardize ) :
    
    - 특정 variable value 따라 model에 영향을 미치는 경우
    ex) 범죄율 (0.1~0.99) 주택 가격( 99 ~ 999 )
    
    - Normalize : variable value 를 일정한 범위로 ( 0 ~ 1 / -1 ~ 1) - > X 변수
        정규화 공식 nor = (x-min) / (max - min)
    
    - standardize : mean , std 를 이용하여                          - > Y 변수
        표준화 공식 z = ( x - mean ) / std

"""

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error , r2_score 

import numpy as np
import pandas as pd

X , y = load_boston(return_X_y = True)
X.shape
y.shape

# datascaling
'''
x normalize => 0 ~ 1
y standardize => mean = 0 , std = 1 
'''

X.max()
X.min()

y.max()
y.mean()

def normal(x):
    nor = (x-np.min(x) / (np.max(x) - np.min(x)))
    return nor

def zscore(y):
    stand = (y-y.mean()) / y.std()
    return stand

x_nor = normal(X)
y_nor = zscore(y)
y_nor
y_nor.mean()
y_nor.std()

# dataset split
x_train , x_test , y_train , y_test = train_test_split(x_nor , y_nor ,random_state = 123) # test_size = 0.25

x_train.shape # (379, 13)

# model 생성
lr = LinearRegression()
model = lr.fit(X = x_train ,y=y_train)
model

# model 평가
y_pred = model.predict(X = x_test )
mse = mean_squared_error(y_test , y_pred) # 0.2933980240643512 오류율
score = r2_score(y_test , y_pred) # 0.6862448857295762 정확률 
score









