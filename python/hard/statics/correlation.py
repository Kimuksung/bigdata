# -*- coding: utf-8 -*-
"""
공분산 vs 상관 계수 분석(correlation)
    - 공통점 : 변수 간의 상관성 분석

1. 공분산 : 두 확률 변수 간의 분산(평균에서 퍼짐 정도)를 나타내는 통계
    - 두 확률 변수 : X , Y -> X 표본 평균( ux) , Y 표본 평균( uy)
    Cov(X,Y) = sum(( X - ux ) * ( Y - uy )) / n
    
    Cov(X,Y) > 0 : X증가 -> Y 증가
    
    Cov(X,Y) < 0 : X증가 -> Y 감소
    
    Cov(X,Y) = 0 : 두 변수는 선형 관계가 아니다.
    
    문제점 : 값이 큰 변수에 영향을 받는다.
    
2. 상관 계수 : 공분산을 각각의 표준 편차로 나누어 정규화한 통계
    - 부호는 공분산과 동일하고, -1 ~ 1 
    - Cor(X,Y) = Cov(X,Y) /( std(x ) *std(Y))

"""

import numpy as np
import pandas as pd

score_iq = pd.read_csv("score_iq.csv")
score_iq.info()

cor = score_iq.corr()
cor
'''         sid     score        iq   academy      game        tv
sid      1.000000 -0.014399 -0.007048 -0.004398  0.018806  0.024565
score   -0.014399  1.000000  0.882220  0.896265 -0.298193 -0.819752
iq      -0.007048  0.882220  1.000000  0.671783 -0.031516 -0.585033
academy -0.004398  0.896265  0.671783  1.000000 -0.351315 -0.948551
game     0.018806 -0.298193 -0.031516 -0.351315  1.000000  0.239217
tv       0.024565 -0.819752 -0.585033 -0.948551  0.239217  1.000000
'''

score_iq['score'].corr(score_iq['iq']) #0.88222034461347

#-----------------------------------------------------------------

'''
1. 공분산
    - score vs iq
    - score vs academy
    
    Cov(X,Y) = sum(( X - ux ) * ( Y - uy )) / n
'''

X = score_iq['score']
Y1 = score_iq['iq']
Y2 = score_iq['academy']


def Cov(x,y):
    ux = x.mean()
    uy = y.mean()
    
    cov_re = sum((x-ux) * (y-uy)) / len(x)
    return cov_re

print(Cov(X,Y1)) #50.99528888888886
print(Cov(X,Y2)) #7.072444444444438

score_iq['score'].cov(score_iq['iq']) # 51.33753914988811

#-----------------------------------------------------------------

'''
2. 상관 계수 
Cor(X,Y) = Cov(X,Y) / (std(x ) *std(Y))
'''

def Cor(x,y):
    cov = Cov(x,y)
    std_x  = x.std()
    std_y = y.std()
    
    return  cov / (std_x * std_y)
    
print(Cor(X,Y1))
print(Cor(X,Y2))



