# -*- coding: utf-8 -*-
"""

Hierachy 군집 분석
    - Bottom up 으로 계층적 군집 형성
    - Uclide 거리 계산식 이용
    - 숫자형 변수만 사용 가능
    

"""

import pandas as pd
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage , dendrogram
import matplotlib.pyplot as plt # 산점도 시각화

# 1. dataset load
iris = load_iris()
iris.feature_names

X = iris.data
y = iris.target

iris_df = pd.DataFrame( X , columns = iris.feature_names)
sp = pd.Series(y)

iris_df['species'] = sp
iris_df.info()

# 2. 계층적 군집 분석
clusters = linkage( iris_df , method = 'complete' , metric= 'euclidean')
'''
method = single : 단순 연결 / complete : 완전 연결 / average : 평균 연결
'''
clusters.shape

# 3. dandrogram visualization
plt.figure( figsize = (10 , 5 ))
dendrogram(clusters , leaf_rotation = 90 , leaf_font_size = 20,)
plt.show()

# 4. cluster 자르기 , 각각의 cluster 특징 분석 : dandrogram의 결과로 판단
from scipy.cluster.hierarchy import fcluster # cluster 자르기

# 1) cluster 자르기
cluster = fcluster(clusters , t = 3 , criterion = 'distance')
cluster

# 2) dataframe 추가
iris_df['cluster'] = cluster
iris_df.head

# 3) 산점도 시각화
plt.scatter(x=iris_df['sepal length (cm)'],y = iris_df['petal length (cm)'], c= iris_df['cluster'],marker = 'o' )

# 4) real data  vs predict data
tab = pd.crosstab(index = iris_df['species'] , columns = iris_df['cluster'] )
tab
'''
cluster   1   2   3
species            
0        50   0   0
1         0   0  50
2         0  34  16
'''


# 5) 군집별 특성 분석
# DF.groupby('집단변수')
cluster_grp = iris_df.groupby('cluster')
cluster_grp.size()
cluster_grp.mean()
'''
         sepal length (cm)  sepal width (cm)  ...  petal width (cm)   species
cluster                                       ...                            
1                 5.006000          3.428000  ...          0.246000  0.000000
2                 6.888235          3.100000  ...          2.123529  2.000000
3                 5.939394          2.754545  ...          1.445455  1.242424
'''






