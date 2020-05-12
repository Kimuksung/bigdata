# -*- coding: utf-8 -*-
"""
sklearn 관련 Linear Regression
"""

from sklearn.linear_model import LinearRegression # model object
from sklearn.model_selection import train_test_split # test /train split
from sklearn.metrics import mean_squared_error,r2_score # model 평가 도구(mse, r2)]
from sklearn.datasets import load_diabetes # dataset

import numpy as np # 숫자 처리

# 단순 선형 회귀

X , y = load_diabetes(return_X_y = True )
X.shape
y.shape
y.mean()

type(X)
# bmi 지수 -> 당뇨병
x_bmi = X[:,2]
x_bmi.shape[0]

#1d -> 2d
x_bmi = x_bmi.reshape(x_bmi.shape[0],1)

# model 생성 : object -> training -> model
obj = LinearRegression() # 생성자 -> object
model = obj.fit(x_bmi , y)

# 예측치
y_predict = model.predict(x_bmi)


# model 평가 : 정규화 되어있다면 -> MSE / 그렇지 않다면r^2
mean_squared_error(y,y_predict) # 3890.4565854612724
r2_sc = r2_score(y,y_predict)
r2_sc # 0.3439237602253803


# train / test 분리 7:3
x_train , x_test , y_train , y_test = train_test_split(x_bmi, y , test_size = 0.3)
x_train.shape

# model 생성 : object -> training -> model
obj = LinearRegression() # 생성자 -> object
model = obj.fit(x_train , y_train)

y_predict = model.predict(x_test)

# y_predict vs y_test
r2_sc = r2_score(y_test,y_predict)
# 0.3863907304530646

import pandas as pd
df = pd.DataFrame({'y_true': y_test , 'y_pred': y_predict})
df.corr()

'''
from scipy import stats
type(x_train)
x_train
model = stats.linregress(x_train,x_test)
'''

import matplotlib.pyplot as plt # virtualization
plt.plot(x_test, y_test , 'ro')
plt.plot(x_test , y_predict , 'b-')
plt.show()

#iris.csv

# 다중 회귀 모델 : y(1) <- x(2~4)

iris = pd.read_csv("iris.csv")
iris.info()

'''
 0   Sepal.Length  150 non-null    float64 y
 1   Sepal.Width   150 non-null    float64 x1
 2   Petal.Length  150 non-null    float64 x2
 3   Petal.Width   150 non-null    float64 x3
 4   Species       150 non-null    object 
'''

# x, y 변수 선택
cols = list(iris.columns)

y_cols= cols[0]
x_cols = cols[1:4]

# dataset split
iris_train , iris_test = train_test_split(iris , test_size = 0.3 ,random_state = 123) # default = 0.25

iris_train.shape #(105, 5)
iris_test.shape # (45, 5)

iris_train.head()

# model 생성
lr = LinearRegression()
model = lr.fit( X = iris_train[x_cols] , y = iris_train[y_cols])
model

# model 평가
y_predict = model.predict(iris_test[x_cols])
y_true = iris_test[y_cols]
df = pd.DataFrame({'y_true': y_true , 'y_pred': y_predict})
df.corr()

# y)true vs y_pred virtualization

import matplotlib.pyplot as plt
fig = plt.figure(figsize = (10,5))
chart = fig.subplots()
chart.plot(np.array(y_true) , color = 'b' ,label = 'real values')
chart.plot(y_predict , color = 'r',label = 'predict values')
plt.show()












