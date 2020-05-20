# -*- coding: utf-8 -*-
"""

Random Forest Hyper parameter

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


rf = RandomForestClassifier()
# model
model = rf.fit(X , y)

###############################
# grid search

from sklearn.model_selection import GridSearchCV

params = {'n_estimators' : [100,200,300,400] , 'max_depth' : [3,6,8,10] , 'min_samples_split' : [2,3,4,5], 
            'min_samples_leaf' : [1,3,5,7]
        }

# 2) gridsearchcv object
gs = GridSearchCV(estimator = model , param_grid = params , scoring = 'accuracy', cv=5 ,n_jobs=1 )

model = gs.fit(X , y)
model.score(X , y )

model.best_params_
# {'svc__C': 1.0, 'svc__gamma': 1.0, 'svc__kernel': 'rbf'}



























