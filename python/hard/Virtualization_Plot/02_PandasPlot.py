# -*- coding: utf-8 -*-
"""
pandas 객체에서 지원하는 시각화
형식) object.plot(kind = 차트 유형)

Object = Series/ DataFrame
kind : bar / barh / pie / hist / kde / box / scatter 

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Series Object virtualization
ser = pd.Series(np.random.randn(10), index=np.arange(0,100,10))
print(ser)

ser.plot(color = "r") # 기본 차트

# 2. DataFrame Object virtualizatiion
df = pd.DataFrame(np.random.randn(10,4) , columns = ['one' , 'two' , 'three', 'four'] )
df
df.shape

# 기본차트
df.plot(kind="bar" , title="bar plot")
df.plot(kind="barh" , title="barh plot")
df.plot(kind="bar" , title="bar plot" ,stacked =True) #누적형
df.plot(kind="hist" , title="histogram") # 도수 분포표(히스토그램)
df.plot(kind="kde" , title="kde plot") # 커널 밀도 추정



tips = pd.read_csv("tips.csv")
tips.info()

# 요일(day) vs 파티 규모(size) 
tips.day.unique()
tips['size'].unique()

# 교차 분할표 : 2개의 집단 변수 이용
tab = pd.crosstab(tips.day , tips['size'])
tab

tab_result = tab.iloc[:,1:5]
tab_result.plot(kind = 'barh', title = 'day vs size', stacked=True)

# 3. 산점도 matrix
from pandas import plotting
iris = pd.read_csv("iris.csv")
iris.info()

cols = list(iris.columns)
iris_x = iris[cols[:4]]

plotting.scatter_matrix(iris_x)

# 4. 3d 산점도
from mpl_toolkits.mplot3d import Axes3D
col1 = iris[cols[0]]
col2 = iris[cols[1]]
col3 = iris[cols[2]]

cdata = []#색상

for i in iris.Species :
    if i=="setosa":
        cdata.append(0)
    elif i=="virginica":
        cdata.append(1)
    else:
        cdata.append(2)

cdata

fig = plt.figure()
chart = fig.add_subplot(1,1,1 , projection = '3d')

chart.scatter(col1, col2, col3 , c=cdata) # (x , y , z)
#(x,y,z,color)

chart.set_xlabel('col1')
chart.set_ylabel('col2')
chart.set_zlabel('col3')

























