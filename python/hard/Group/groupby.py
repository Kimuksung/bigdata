# -*- coding: utf-8 -*-
"""
DataFrame object
    - form) DF[column].groupby('value').math/statistic function()

"""

import pandas as pd

tips = pd.read_csv("tips.csv" , encoding = 'utf-8')
tips.info()

tips.head()

# 팁에 대한 비율 : 파생 변수

tips['tip_pct'] = tips.tip / tips.total_bill
tips.info()
tips.head()

# column name 변경
# 복제 후 삭제
tips['gender'] = tips['sex']
del tips['sex']

tips.info()
tips.head()

#1 one value grouping
gender_grp =  tips.groupby('gender')

gender_grp.size() #frequency

gender_grp.sum()

gender_grp.mean()

gender_grp.describe() # 각 그룹별 요약 통계치

gender_grp.boxplot()

#2 one value grouping -> select column grouping

smoker_grp = tips['tip'].groupby(tips['smoker'])
smoker_grp.size()

smoker_grp.mean()

#3 two value grouping
# df.groupby([column , column])

gender_smoker_grp = tips.groupby(['gender', 'smoker'])
gender_smoker_grp.size()

# 특정 변수 통계량
gender_smoker_grp['tip'].describe()
# 여성은 흡연자가 ,남성은 비흡연자가 팁 지불에 더 후하다.

#4 two value -> select column grouping
gender_smoker_tip_grp = tips['tip'].groupby([tips['gender'], tips['smoker']])
gender_smoker_tip_grp.size()
gender_smoker_tip_grp.size().shape

# 각 집단별 tip 합
gender_smoker_tip_grp.sum()
gender_smoker_tip_grp.sum().shape #(4,)

# 1d -> 2d (교차 분할표)
grp_2d = gender_smoker_tip_grp.sum().unstack()
grp_2d.shape #(2, 2)


# 2d -> 1d
grp_1d = grp_2d.stack()
grp_1d.shape


# 성별 vs 흡연 유무 -> 교차분할표(빈도수)
grp_2d_size = gender_smoker_tip_grp.size().unstack()
grp_2d_size

# iris dataset 그룹화
iris = pd.read_csv("iris.csv")

iris.info()

iris.groupby('Species').sum()
iris['Sepal.Length'].groupby(iris['Species']).sum()





















