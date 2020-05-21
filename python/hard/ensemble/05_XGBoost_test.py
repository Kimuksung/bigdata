# -*- coding: utf-8 -*-
"""

XGBoost model

"""

from xgboost import XGBClassifier , XGBRegressor
from xgboost import plot_importance

from sklearn.datasets import make_blobs # cluster dataset create
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , classification_report

import matplotlib.pyplot as plt

# 1. dataset load
X , y = make_blobs( n_samples = 2000 , n_features = 4 , centers = 2 , cluster_std = 2.5)
'''
n_samples : dataset 크기
n_features : X variable
centers : Y category 갯수
cluster_std : cluster 표준편차(높을 수록 많이 겹친다.)
'''

X.shape
X
y.shape
y

plt.scatter(x = X[:, 0 ] , y = X[:,1] , s = 100 , c = y, marker ='o')

# 2. train , test set
# XGboost model
x_train , x_test , y_train , y_test = train_test_split(X , y ,test_size = 0.3)

# 3. model 생성
xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)
model
# binary : logistic -> 이항 분류
# multi : softmax

y_pred = model.predict(x_test )
accuracy_score(y_test , y_pred)

print(classification_report(y_test , y_pred))

# 4. 중요 변수 시각화
fscore = model.get_booster().get_fscore()
plot_importance(model)
plt.show()

xgb




















