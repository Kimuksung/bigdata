# -*- coding: utf-8 -*-
"""
행렬 곱 함수(np.dot) 이용 y 예측치 구하기
y = np.dot(X,a) + b
 
"""

from scipy import stats #단순 회귀 모델
from statsmodels.formula.api import ols # 다중 회귀 모델
import pandas as pd

# 1. dataset load
score = pd.read_csv("score_iq.csv")
score.info()

# score = y iq = x1  academy =x2

formula = "score ~ iq + academy"

model = ols(formula, data =score).fit()
model.params
'''
Intercept    25.229141
iq            0.376966
academy       2.992800
'''
model.summary()

# Adj. R-squared:                  0.946
# F-statistic:                     1295.
# Prob (F-statistic):           4.50e-94

#library를 이용한 예측
model.fittedvalues #예측치

#y = np.dot(X,a) + b

X = score[['iq','academy']]
X

import numpy as np
a = np.array([[0.376966],[2.992800]])
a = [[0.376966],[2.992800]]
a.shape
b = model.params.Intercept

y_pred2 = np.dot(X ,a) + b
y_pred=y_pred2.reshape(150)
y_pred.shape
y_true = score.score
y_true.shape
df = pd.DataFrame({'y_true': y_true , 'y_pred': y_pred})

df.corr()
