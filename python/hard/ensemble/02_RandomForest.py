# -*- coding: utf-8 -*-
"""

Random Forest Ensemble model


"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.metrics import confusion_matrix , accuracy_score , classification_report

# 1. dataset load
wine = load_wine()
wine.feature_names # x variable names
wine.target_names # y variable names

X = wine.data
y = wine.target

# model
rf = RandomForestClassifier()

'''
n_estimators (default=100) - tree 수
criterion (default="gini") - 중요 변수(gini, entropy ) 선정
max_depth (default=None) - tree depth
min_samples_split (default=2) - 노드 분할 최소 sample 수
min_samples_leaf (default=1) - terminal node 분할 최소 sample 수
max_features (default="auto") - max x variable
n_jobs - cpu num
random_state - seed create
'''
import numpy as np
idx = np.random.choice(a = X.shape[0] , size = int(X.shape[0]*0.7) , replace=False)

x_train = X[idx]
y_train = y[idx]

model = rf.fit(x_train , y_train)

idx_test= [ i for i in range(len(X)) if not i in idx]

x_test = X[idx_test]
y_test = y[idx_test]

y_true = y_test
y_pred = model.predict(x_test)

con_mat = confusion_matrix(y_true , y_pred)
acc = accuracy_score(y_true , y_pred)
report = classification_report(y_true , y_pred)

con_mat
acc
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        18
           1       1.00      0.96      0.98        26
           2       0.91      1.00      0.95        10

    accuracy                           0.98        54
   macro avg       0.97      0.99      0.98        54
weighted avg       0.98      0.98      0.98        54
'''
model.feature_importances_

# 중요 변수 시각화
import matplotlib.pyplot as plt
x_size = X.shape[1]
plt.barh( range(x_size) , model.feature_importances_)
plt.yticks(range(x_size) , wine.feature_names)
plt.show()













