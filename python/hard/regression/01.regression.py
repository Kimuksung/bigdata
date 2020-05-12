# -*- coding: utf-8 -*-
"""
회귀 방정식에서 기울기(slope) 와 절편(intercept)

     기울기(slope) = Cov(x,y) / Sxx (x의 편차 제곱)
     절편(intercept) = y_mu - (slope * x_mu)
"""

from scipy import stats
import pandas as pd

galton = pd.read_csv("galton.csv")
galton.info()

# parent (x) --> child(y)
x = galton['parent']
y = galton['child']

model = stats.linregress(x,y)
model

'''
slope=0.6462905819936423, 
intercept=23.941530180412748, 
rvalue=0.4587623682928238,  # 설명력
pvalue=1.7325092920142867e-49, 
stderr=0.04113588223793335)
'''

y_pred = x*model.slope +model.intercept
y_pred
y_true = y

# 예측치 vs 관측치(정답)
y_pred.mean()
y_true.mean()

# 기울기 계산 =Cov(x,y)  / Sxx(x의 편차 제곱 평균)


xu = x.mean()
yu = y.mean()
Cov_xy = sum((x-xu) * (y - yu)) / len(x)
Sxx = np.mean((x - xu)**2)
Sxx
slope = Cov_xy / Sxx
slope

# 2. 절편 계산식
# y_mu - (slope * x_mu)

intercept = yu - (slope * xu)
intercept

# 3. 설명력( rvalue)
galton.corr()


y_pred = x * slope + intercept
y_pred.mean()
y.mean()











