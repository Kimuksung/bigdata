# -*- coding: utf-8 -*-
"""

Gini Impurity(불순도) / Entropy
    - tree model important variable 선정 기준
    - 정보이득 = base 지수 - Gini 불순도 or entropy
    - 정보이득이 클 수록 중요변수로 본다.
    - Gini impurity = sum(p * (1-p))
    - Entropy = -sum(p * log(p))
"""

import numpy as np

# 1. 불확실성이 큰 경우
x1 = 0.5
x2 = 0.5
# 전체 확률 = 1

gini = sum([x1 * (1-x1) , x2*(1-x2)])
gini

entropy = -sum([ x1 * np.log2(x1), x2 * np.log2(x2)])
entropy


'''

cost(loss) function : 정답과 예측치 -> 오차 반환 함수
x1 -> y_true , x2-> y_pred
y_true = x1 * np.log(x1)
y_pred = x2 * np.log(x2)

'''

y_true = x1 * np.log2(x1)
y_pred = x2 * np.log2(x2)
cost = -sum([y_true , y_pred])
cost

# 2. 불확실성이 작은 경우
x1 = 0.9
x2 = 0.1
# 전체 확률 = 1

gini = sum([x1 * (1-x1) , x2*(1-x2)])
gini # 0.18

entropy = -sum([ x1 * np.log2(x1), x2 * np.log2(x2)])
entropy # 0.4689955935892812

##############################
# dataset 적용
##############################

def createDataSet():
    dataSet = [[1, 1, 'yes'],
    [1, 1, 'yes'],
    [1, 0, 'no'],
    [0, 1, 'no'],
    [0, 1, 'no']]

    columns = ['dark_clouds','gust'] #X1,X2,label
    return dataSet, columns
dataSet, columns = createDataSet()

dataSet = np.array(dataSet) # list -> numpy
columns 
dataSet.shape

X = dataSet[:, :2]
y = dataSet[:, -1]

X
y 

# dummy
y = [1 if t =='yes' else 0 for t in y]
y

from sklearn.tree import DecisionTreeClassifier , export_graphviz
from sklearn.metrics import accuracy_score

dt = DecisionTreeClassifier('entropy')
model = dt.fit(X , y)

pred = model.predict(X)
accuracy_score(y , pred) # 1.0

from sklearn import tree
tree.plot_tree(model)
export_graphviz(model , out_file = 'dataset_tree.dot' , max_depth = 3 , feature_names = columns)
















