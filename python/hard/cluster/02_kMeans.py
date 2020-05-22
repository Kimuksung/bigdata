# -*- coding: utf-8 -*-
"""

Kmeans 알고리즘
    - 비계층적 군집분석
    - 군집수(k) 알고 있는 경우
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans # model
#from sklearn.cluster import k_means
import matplotlib.pyplot as plt

# 1. dataset

# text file -> numpy
def dataMatrix(file) :
    dataset=[]
    f = open(file, mode = 'r') # file object
    lines = f.readlines()
    for line in lines : 
        a,b = line.split('\t')
        dataset.append([float(a) , float(b)])
    
    return np.array(dataset)

dataset = dataMatrix("testSet.txt")
dataset.shape

# numpy -> pandas
df = pd.DataFrame(dataset , columns = ["x", "y"])

# 2. Kmeans model
kmeans = KMeans( n_clusters = 4 , algorithm = 'auto')
kmeans
model = kmeans.fit( df )
pred = model.predict(df)
pred

# 3. virtualization
df['cluster'] = pred
df.info()

plt.scatter(x = df['x'],y = df['y'],c=df['cluster'],marker = 'o')

# each cluster의 center
centers = model.cluster_centers_
plt.scatter(x = centers[:,0],y = centers[:,1],c='red',marker = 'D')

grp = df.groupby('cluster')
grp.mean()
'''
                x         y
cluster                    
0        2.626530  3.108680
1       -3.382370 -2.947336
2        2.802931 -2.731515
3       -2.461543  2.787376
'''


















