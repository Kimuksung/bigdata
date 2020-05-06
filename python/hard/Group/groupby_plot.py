# -*- coding: utf-8 -*-
"""
집단 변수 기준 자료 분석
    - subset 생성
    - group 객체 생성
    - 시각화

"""

import pandas as pd


# 1. dataset load
wine = pd.read_csv("winequality-both.csv" , encoding = "utf-8")
wine.head()
wine.info()

# 칼럼명 변경 : 공백 -> '_' 교체
wine.columns = wine.columns.str.replace(" " , "_")
wine.info()

#집단 변수 확인
wine.type.unique() # ['red', 'white']
wine.quality.unique() #[5, 6, 7, 4, 8, 3, 9]

# 2. subset 생성

# 1) type column : DataFrame
red_wine = wine.loc[ wine['type']=='red' , : ]
red_wine.info()
red_wine.shape

red_wine
# 2) type(행) vs quality(렬)
red_qual = wine.loc[wine['type']=='red' , 'quality']
red_qual
red_qual.shape

white_qual = wine.loc[wine['type']=='white' , 'quality']
white_qual
white_qual.shape

# 3. group object 생성 : 집단 변수 2개 -> 11변수 그룹화
wine_grp = wine.groupby([wine['type'], wine['quality']])
type(wine_grp)
wine_grp.size()

# 1d -> 2d
grp_2d = wine_grp.size().unstack()
grp_2d
 
# 교차 분할표
tab = pd.crosstab(wine['type'] , wine['quality']) #(index = 행, column = 열)
tab

# 4. group 객체 시각화
import matplotlib.pyplot as plt

type(grp_2d)

grp_2d.plot(kind = 'barh' , title = "type vs quality" , stacked=True)

plt.show()

# 5. wine 종류(집단 변수) vs 알코올(연속형) 통계량
wine_grp = wine.groupby('type')

wine_grp['alcohol'].describe()
    






















