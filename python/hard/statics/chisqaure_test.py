# -*- coding: utf-8 -*-
"""
카이 제곱 검정
    - 일원 카이 제곱 , 이원 카이 제곱
"""

from scipy import stats
import numpy as np

# 1. 일원 카이제곱 검정
real_data = [4, 6, 17, 16, 8, 9] # 관측치
exp_data = [10,10,10,10,10,10] # 기대치
chis = stats.chisquare(real_data, exp_data)
chis
# statistic=14.200000000000001, pvalue=0.014387678176921308
# statistic = χ2 = Σ (관측값 - 기댓값)2 / 기댓값

# list -> numpy
real_arr = np.array(real_data)
exp_arr = np.array(exp_data)

chis2 = sum((real_arr - exp_arr) **2 / exp_data)
chis2

# 2. 이원 카이제곱 검정
import pandas as pd
smoke = pd.read_csv("smoke.csv")
smoke.info()
smoke

'''
 교육 수준 vs 흡연 여부 독립성 검정
 귀무 가설 : 교육 수준과 흡연 여부는 상관관계가 없다.
'''

# DF -> vector
education = smoke.education
smoking = smoke.smoking

# cross table
table = pd.crosstab(education , smoking)
table


chis = stats.chisquare(education,smoking)
chis # statistic=347.66666666666663, pvalue=0.5848667941187113

#pvalue>=0.05 -> 귀무 가설 채택

'''
성별과 흡연 여부
'''

tips = pd.read_csv("tips.csv")
tips.info()
smoker = tips.smoker
sex = tips.sex

pd.crosstab(smoker,sex)

#smoker = smoker[if smoker=="No": 0 else:1]
#dummy 변수 설정
smoker = [1 if i=="No" else 2 for i in smoker]
sex = [1 if i=="Female" else 2 for i in sex]

chis = stats.chisquare(smoker,sex)
chis
# statistic=81.5, pvalue=1.0










