# -*- coding: utf-8 -*-
"""
Dataframe 병합 merge
"""

import pandas as pd

# 1. Series merge
s1 = pd.Series([1,3], index=['a','b'])
s2 = pd.Series([5,6,7], index=['a','b','c'])
s3 = pd.Series([11,13], index=['a','b'])

# 행 단위 결합 rbind()
s4 = pd.concat([s1,s2,s3] , axis=0)
s4.shape

s5 = pd.concat([s1,s2,s3] , axis=1)
s5.shape

# 2. DataFrame Merge
wdbc = pd.read_csv("C:\\ITWILL\\4_Python-II\\data/wdbc_data.csv" , encoding='utf-8')
wdbc.info()

# DF1(16) + DF2(16)
cols = list(wdbc.columns)
cols1 = cols[:16]
cols2 = cols[16:]

df1 = wdbc[cols1]
df1.shape
df2 = wdbc[cols2]
df2.shape

df2[id] = wdbc.id
df2.shape
'''
# Merge = 공통되는 column가 있는 경우
pd.merge(df1, df2)

'''
# concat = 결합하는 경우
df1 = wdbc[cols1]
df1.shape
df2 = wdbc[cols2]
df2.shape

df3 = pd.concat([df1, df2] , axis = 0) # 열 단위 결합
df3.info
#df3.shape







