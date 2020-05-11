# -*- coding: utf-8 -*-
"""

집단 간 평균 차이 검정(t-test)
    1. 한 집단 평균 차이 검정
    2. 두 집단 평균 차이 검정
    3. 대응 두 집단 평균 차이 검정
    

"""

from scipy import stats

import numpy as np
import pandas as pd

# 1. 한 집단 평균 차이 검정

# 대한민국 남자 평균 키 ( 모평균 ) : 175.5cm
# 모집단 -> 표본 추출( N명 ) 

sample_data = np.random.uniform(172 , 180, 300) #300명 랜덤
sample_data

# 기술 통계
sample_data.mean() #175.9014855814808

one_group_test = stats.ttest_1samp(sample_data , 175.5 )
one_group_test

print('statics = %.5f , pvalue = %.5f'%(one_group_test))
# statics = 2.99767 , pvalue = 0.00295

# 2. 두 집단 평균 차이 검정

female_score = np.random.uniform(50, 100 , size = 30)
male_score = np.random.uniform(45, 95 ,size=30)

two_sample = stats.ttest_ind(female_score , male_score)
two_sample
# (statistic=0.3713812698223998, pvalue=0.7117068000958077) >= 0.05
print('statics = %.5f , pvalue = %.5f'%(one_group_test))

# 기술 통계
female_score.mean() #73.8826774529227
male_score.mean() #72.47439180089641

# csv_file_load
two_sample = pd.read_csv("two_sample.csv")
two_sample.info()

# 교육방법 , score만 필요
# 집단 변수 method 
sample_data =two_sample[['method','score']]
sample_data.head()
sample_data['method'].value_counts()
'''
2    120
1    120
'''

method1 = sample_data[sample_data['method']==1]
method2 = sample_data[sample_data['method']==2]


score1 = method1.score
score2 = method2.score

# Na 제거(평균 제거)
score1 = score1.fillna(score1.mean())
score2 = score2.fillna(score1.mean())

stats.ttest_ind(score1 , score2)
# statistic=-0.7254392243734085, pvalue=0.4688953070379147

# 기술 통계량
score1.mean()
score2.mean()

# 3. 대응 두 집단 평균 차이 검정 : 복용 전 65 -> 복용 후 60
before = np.random.randint(65 , size = 30) * 0.5
after = np.random.randint(60 , size = 30) * 0.5


pired_test = stats.ttest_rel( before , after )
pired_test
# statistic=-0.9078497931862818, pvalue=0.3714403781170247

before.mean()
after.mean()































