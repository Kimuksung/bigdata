# -*- coding: utf-8 -*-
"""
- DataFrame의 요약 통계량
- 상관계수
"""

import pandas as pd

product = pd.read_csv("C:\\ITWILL\\4_Python-II\\data/product.csv" , encoding ='utf-8')
product.info()
product.head()

# 요약 통계량
summary = product.describe()
print(summary)

# 행/렬 통계
product.sum(axis=0)
product.sum(axis=1)


tmp = [[1,2,3],[4,5,6],[7,8,9]]

# 산포도 : 분산 , 표준 편차
product.var() #axis=0
product.std()
product

# 빈도수 : 집단 변수
a_cnt = product['a'].value_counts()
type(a_cnt)
a_cnt[3]

# 유일값 보기
product['c'].unique()

# 상관관계
product.corr() #상관계수 행렬

#iris 상관관계 비교
iris = pd.read_csv("C:\\ITWILL\\4_Python-II\\data/iris.csv" , encoding = "utf-8")
iris
iris_df = iris.iloc[:,:4]
iris_df.shape
iris_df.corr()
iris_df.describe() #요약 통계량
# value count는 int형이 아니기 때문에 안하는게 낫다.

species = iris.Species
species.value_counts()
species.unique()
list(species.unique())




















