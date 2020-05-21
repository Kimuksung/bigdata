# -*- coding: utf-8 -*-
"""

1. XGBoost Hyper Parameter
2. model 학습 조기종료 : early stopping rounds
3. Best Hyper Parameter : Grid Search

"""

from xgboost import XGBClassifier
from sklearn.datasets import make_blobs # 다항 분류
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , classification_report

# 1. XGBoost Hyper Parameter
X , y = make_blobs( n_samples = 2000 , n_features = 4 , centers = 3 , cluster_std = 2.5)

X.shape
y

x_train , x_test , y_train , y_test = train_test_split(X , y ,test_size = 0.3)

xgb = XGBClassifier()
model = xgb.fit(x_train, y_train)

model
'''
colsample_bylevel = 1 : 트리 모델 생성시 훈련 셋 샘플링 비율 ( 1 -> 100% )
learning_rate=0.300000012 : 학습율 ( 0.01 ~ 0.1)
max_depth=6 : 트리의 깊이, 과적합 영향
min_child_weight = 1 : 자식 노드 분할 결정하는 최소 가중치의 합
n_estimators=200 : 학습 tree model 수
objective='multi:logistic'  이항 분류 다항 분류 결정(Y를 보고 자동 결정)
'''

# 2. model 학습 조기종료 : early stopping rounds
eval_set = [(x_test , y_test)] # 평가셋
model_early = xgb.fit(x_train , y_train , eval_set = eval_set , eval_metric = 'merror' , early_stopping_rounds = 100 , verbose = True)
'''
X, y : 훈련 셋
eval_set : 평가 셋
eval_metric : 평가 방법 (이항 분류 -> error 다항 분류 -> merror 회귀->rmse)
early_stopping_rounds : 학습 조기 종료
verbose : 학습 과정 출력 여부
'''

model_early.score(x_test , y_test) # 0.95

# 3. Best Hyper Parameter : Grid Search
from sklearn.model_selection import GridSearchCV

xgb = XGBClassifier()

params = { 'colsample_bylevel' : [0.6 , 0.8 , 1.0] , 'learning_rate' : [ 0.01 , 0.05 , 0.1 , 0.5],
'max_depth' : [3,5,7] , 'min_child_weight' : [1,3,5] , 'n_estimators' :[100 ,300 , 500]
        }

gs = GridSearchCV(estimator = xgb , param_grid = params , cv = 5)
model = gs.fit(x_train , y_train , eval_set = eval_set ,eval_metric = 'error' , verbose = True)
model_early.score(x_test , y_test) # 0.9766081871345029
model.best_params_
'''
{'colsample_bylevel': 0.6,
 'learning_rate': 0.5,
 'max_depth': 3,
 'min_child_weight': 1,
 'n_estimators': 100}
'''



















