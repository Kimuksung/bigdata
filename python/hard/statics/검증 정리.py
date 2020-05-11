# -*- coding: utf-8 -*-
"""
test 관련

all data = population
data를 sampling 하게 되면 정규성 검증을 한다.
data가 정규성 검증을 통해 정규성을 띄게 되면 모수 기법 / 아니면 비모수 기법


모수 기법

- 정규성 검정
scipy stats를 이용
1. shapiro
2. kstest

- 이항 분포 검정
1. binomtest

- 카이 제곱 검정(포아송)
1. chisquare

- T 검정  = 2개의 집단을 비교할 때 사용(평균)
1. ttest-lsamp =모평균을 알고 있어야 하며, sample의 평균을 이용하여 검정
2. ttest_ind = 서로 다른 두 집단의 평균을 비교하여 검정
3. ttest_rel = 대응 되는 두 집단의 평균을 비교하여 검정

- anova 검정 = T검정과 비슷하지만,  3개 이상의 집단을 비교할 때 사용 / 분산 값이 크게 되면 평균에 영향을 미침으로 
1. 

Ex) 카페에서 아메리카노 선호도를 조사 할 때에 남녀 선호도 비교 -> t-test
                                    20대, 30대,40대,50대 선호도 비교 -> anova
"""

import scipy.stats as stats
import pandas as pd
import urllib
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import numpy as np

'''
centers = [5,5.3,4.5]
std = 0.1
colors = 'brg'

data_1 = []
for i in range(3):
    data_1.append(stats.norm(centers[i], std).rvs(100))
    plt.plot(np.arange(len(data_1[i]))+i*len(data_1[0]),data_1[i], '.', color = colors[i])
'''


url = 'https://raw.githubusercontent.com/thomas-haslwanter/statsintro_python/master/ipynb/Data/data_altman/altman_910.txt'
data = np.genfromtxt(urllib.request.urlopen(url), delimiter=',')
# 귀무 가설 : 그룹의 평균값이 통계적으로 의미가 없다.


# Sort them into groups, according to column 1
group1 = data[data[:,1]==1,0]
group2 = data[data[:,1]==2,0]
group3 = data[data[:,1]==3,0]

# matplotlib plotting
plot_data = [group1, group2, group3]
ax = plt.boxplot(plot_data)
plt.show()

F_statistic, pVal = stats.f_oneway(group1, group2, group3)
# pvalue = 0.043589334959178244 < 0.05 가무 귀설 기각
# 그룹의 평균값이 통계적으로 의미가 있다.






