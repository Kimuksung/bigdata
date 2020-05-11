# -*- coding: utf-8 -*-
"""
회귀 분석

scipy package의 stats module function
- 통계적 방식의 회귀 분석

1. 단순 선형 회귀 모델

2. 다중 선형 회귀 모델

"""

from scipy import stats # 회귀 모델 생성
import pandas as pd

# 1. 단순 선형 회귀 모델
'''
x-> y 
''' 

score_iq = pd.read_csv("score_iq.csv")
score_iq.info()

x=score_iq.iq
y=score_iq['score']

# 회귀 모델 생성
model = stats.linregress(x,y)
model
'''
# slope=0.65143095272700 : 기울기
# intercept=-2.8564471221974657:절편
# rvalue=0.882220344613469 : 설명력
# pvalue=2.8476895206683644e-50 : x의 유의서 검정
# stderr=0.028577934409305443 :표본 오차

'''

score_iq.head(1)
#     sid  score(Y)   iq(X)  academy  game  tv

X = 140
# y = X * a + b
y_pred = X * model.slope + model.intercept
y_pred

y_real = 90
err = y_real - y_pred
err # 1.6561137404164157

#################
# product.csv
#################

product = pd.read_csv("product.csv")
product.info()

product.corr()

# x = 제품 적절성 vs y = 제품의 만족도
model2 = stats.linregress(product['b'] , product['c'])

'''
slope=0.7392761785971821, 
intercept=0.7788583344701907, 
rvalue=0.766852699640837, 
pvalue=2.235344857549548e-52, 
stderr=0.03822605528717565
'''

product.head(1)
'''
   a  b  c
0  3  4  3
'''
x=4
y_pred =  model2.slope * x + model2.intercept
y_pred # 3.735963048858919

# err는 음수로 나올수도 있기 때문에 제곱으로
y=3
err = (y - y_pred) **2

X = product['b']
y_pred = X * model2.slope  + model2.intercept
y= product['c']

error = y - y_pred
sum(error**2) # 74.40922998967092

# 2. 회귀 모델 시각화
from pylab import plot,legend,show

plot(product['b'],product['c'] , 'b.') #(x,y )산점도
plot(product['b'],y_pred , 'r.-')
legend(['x,y scatter', 'regress model line'] )
show()


# 3. 다중 선형 회귀 모델 y ~ x1+ x2 ...
from statsmodels.formula.api import ols

wine = pd.read_csv("winequality-both.csv")
wine.info()

wine.columns = wine.columns.str.replace(" ", "_")
wine.info()

# quality vs other (alcohol , volatile_acidity ,chlorides )
cor = wine.corr()
cor.quality

formula = "quality ~ alcohol + volatile_acidity + chlorides"

model = ols(formula , data = wine).fit()

model.summary()
'''
Adj. R-squared:                  0.259  # 설명력
F-statistic:                     758.6
Prob (F-statistic):               0.00 < 0 .05 # 모델 유의성 검정 
'''

model.params # 기울기 절편


# y의 예측치 vs 관측치
y_pred = model.fittedvalues
y_true = wine['quality']

err = (y_true - y_pred)**2
err

y_true[:10]
y_pred[:10]


y_true.mean()
y_pred.mean()


# 차트 시각화
import matplotlib.pyplot as plt
plt.plot(y_true[:10],'b',label='real values')
plt.plot(y_pred[:10],'r',label='y_prediction')
plt.yticks(range(0,10))
plt.legend(loc='best')
plt.show
    






