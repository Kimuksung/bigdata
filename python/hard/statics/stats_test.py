# -*- coding: utf-8 -*-
"""

scipy package 확률 분포

1. 정규 분포 검정
    - continous 확률 분포 : 정규 분포 , 균등 분포 , 카이제곱 , T/Z/F 분포
2. 이항 분포 검정
    - descrete 확률 분포 : 베르누이분포 , 이항 분포 , 포아송 분포

"""

from scipy import stats # 확률 분포 검정
import numpy as np
import matplotlib.pyplot as plt

# 1. 정규 분포 검정 : 평균 중심 좌우 대칭성

# 1) 정규 분포 객체 생성
mu = 0 ; std = 1 #표준 정규 분포
std_norm = stats.norm(mu , std) # 정규 분포 객체 생성
std_norm

# 2) 정규 분포 확률 변수
norm_data = std_norm.rvs(1000) # 1000개의 난수 생성
norm_data2 = std_norm.rvs(10000)
len(norm_data)

# 3) histogram
plt.hist(norm_data)
plt.show()

# 4) 정규성 검정
# 귀무가설 : 정규 분포와 차이가 없다.
test_stats , pvalue = stats.shapiro(norm_data) # (  검정 통계량 0.9986441731452942, pvalue = 0.650850236415863)
stats.kstest(norm_data,'norm')
stats.kstest(norm_data2, 'norm')   
'''
검정 통계량 : 0.99854 -> -1.9 ~ 1.96 채택역
pvalue : 0.65 >= 0.5(a) 채택역

'''
# 2. 이항 분포 검정 : 범주의 확률 분포 + 가설 검정

'''
베르누이 분포: 이상 변수에서 성공이 나올 확률 분포(모수:성공 확률)
이항 분포 :베르누이 분포에 시행횟수 N 을 적용한 확률 분포( 모수 : P , N)

Ex) 게임에 이길 혹률(40%) , 시행 횟수: 100번
'''
N = 100
p = 0.4

# 1) 베르누이 분포 확률 변수
x = stats.bernoulli(p).rvs(N)

# 2) 성공 횟수
x_succ = np.count_nonzero(x)
x_succ #38

# 3) 이항 분포 검정: 이항 분포에 대한 가설 검정
# 귀무가설 : 게임에 이길 확률은 40%와 다르지 않다.
pvalue = stats.binom_test( x = x_succ , n = N , p = 0.4 , alternative = 'two-sided')
'''
x : 성공횟수
n : 시행 횟수
p : 성공 확률
two-sided : 양측 검정
'''

pvalue #0.7596549811610628
if pvalue >= 0.05 :
    print("귀무 가설 채택")
else:
    print("귀무 가설 X -> 다르다")


'''
100명의 합격자 중에서 남자 합격자는 45 일 때 남녀 합격률에 차이가 있다고 할 수 있는가?

'''

# 남녀 합격률에 차이가 없다. ( p = 0.5)
N = 100
p = 0.5

pvalue = stats.binom_test(45 , N)
pvalue #0.36820161732669654

if pvalue > 0.05:
    print("귀무 가설 채택 남녀 합격률에 차이가 없다.")




    
    
    















