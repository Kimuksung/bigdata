# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime , timedelta
from sklearn.metrics import classification_report

plant1_train = pd.read_csv('plant1_train.csv')
plant2_train = pd.read_csv("plant2_train.csv")

plant1_train = plant1_train.drop('Unnamed: 0' , axis=1)
cols = ['Date' , 'loc1_tem', 'loc1_hum', 'loc1_coil_temp','loc2_tem', 'loc2_hum', 'loc2_coil_temp' , 'loc3_tem', 'loc3_hum', 'loc3_coil_temp', 'out_tem', 'out_hum', 'loc1' , 'loc2' , 'loc3']
plant1_train.columns = cols

# data preprocessing
plant1_train_first = plant1_train[['Date','loc1_tem', 'out_tem' , 'loc1_coil_temp','loc1_hum' ,'out_hum','loc1']]

a = datetime.strptime(plant1_train_first['Date'][0]  , '%Y-%m-%d %H:%M')

date_trans = []
for i in range(0,len(plant1_train_first)):
    date_trans.append(datetime.strptime(plant1_train_first['Date'][i] , '%Y-%m-%d %H:%M'))

plant1_train_first['date_trans'] = date_trans
plant1_train_first

hour24 = []
for i in range(0,len(plant1_train_first)):
    tmp = datetime.strptime(plant1_train_first['Date'][i]  , '%Y-%m-%d %H:%M') + timedelta(days=1)
    tmp1 = datetime.strptime(plant1_train_first['Date'][i]  , '%Y-%m-%d %H:%M')
    if(len(plant1_train_first[plant1_train_first['date_trans']==tmp]) > 0 ):
        loc_24hour = plant1_train_first[plant1_train_first['date_trans']==tmp]
        print(plant1_train_first['Date'][i])
        print(loc_24hour['Date'])
        print("this", float(loc_24hour['loc1'].values))
        print("-"*10)
        hour24.append(float(loc_24hour['loc1'].values))
    else:
        hour24.append(float('NaN'))

plant1_train_first['24hourloc'] = hour24
plant1_train_first

plant1_train_first_24 = plant1_train_first.dropna(axis=0)
plant1_train_first_24[plant1_train_first_24['24hourloc']==1]
plant1_train_first_24.columns

# balanced sampling (downsampling) 267 vs 500
plant1_train_first_24_true = plant1_train_first_24[plant1_train_first_24['24hourloc']==1]
plant1_train_first_24_false = plant1_train_first_24[plant1_train_first_24['24hourloc']==0]

plant1_train_first_24_true.shape # (267, 9)
plant1_train_first_24_false.shape # (57133, 9)

plant1_train_first_24_true = plant1_train_first_24_true.drop(['Date', 'loc1_tem', 'out_tem', 'out_hum','loc1', 'date_trans'], axis=1)
plant1_train_first_24_false = plant1_train_first_24_false.drop(['Date', 'loc1_tem', 'out_tem', 'out_hum','loc1', 'date_trans'], axis=1)

plant1_train_first_24_false_sample = plant1_train_first_24_false.sample(500)

plant1_train_first_24_false_sample

plant1_balancedsample = pd.concat([plant1_train_first_24_true, plant1_train_first_24_false_sample])
plant1_balancedsample

# balanced sampling(downsampling) + Decision Tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score  , confusion_matrix

x_cols = plant1_balancedsample.columns[:2]
y_cols = plant1_balancedsample.columns[-1]

dtc = DecisionTreeClassifier(max_features = 'auto' , criterion = "gini", max_depth=3 ,splitter = 'best' , min_samples_split=3 , min_samples_leaf = 9)
# =============================================================================
# class_weight             None
# criterion                gini
# max_depth                   3
# max_features             auto
# min_samples_leaf            9
# min_samples_split           3
# splitter                 best
# mean_test_score      0.820321
# Name: 2064, dtype: object
# =============================================================================
model = dtc.fit(X = plant1_balancedsample[x_cols],y = plant1_balancedsample[y_cols])

plant1_sample = pd.concat([plant1_train_first_24_true , plant1_train_first_24_false])
y_pred = model.predict(plant1_sample[x_cols])
confusion_matrix(plant1_sample[y_cols], y_pred)
# =============================================================================
# array([[55436,  1697],
#        [  108,   159]]
# =============================================================================
print(classification_report(plant1_sample[y_cols], y_pred))
# =============================================================================
#               precision    recall  f1-score   support
# 
#          0.0       1.00      0.97      0.98     57133
#          1.0       0.09      0.60      0.15       267
# 
#     accuracy                           0.97     57400
#    macro avg       0.54      0.78      0.57     57400
# weighted avg       0.99      0.97      0.98     57400
# =============================================================================


# grid search
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import numpy as np

dt_clf = DecisionTreeClassifier()
parameters = {'criterion': ['gini', 'entropy'],
              'max_depth': [3, 5, 7, 9],
              'min_samples_split': [x for x in range(3, 15,2)],
              'min_samples_leaf': [x for x in range(1, 15,2)],
              'max_features': ['auto', 'sqrt', 'log2'],
              'class_weight': ['balanced', None],
              'splitter': ['best', 'random']}

grid_dt = GridSearchCV(dt_clf, # estimator 객체,
                      param_grid = parameters, cv = 5,
                      # n_jobs = -1: 모든 cpu를 사용)
                      )

grid_dt.fit(X = plant1_balancedsample[x_cols],y = plant1_balancedsample[y_cols])

result = pd.DataFrame(grid_dt.cv_results_['params'])
result['mean_test_score'] = grid_dt.cv_results_['mean_test_score']
result.sort_values(by='mean_test_score', ascending=False).iloc[0,:]
# =============================================================================
# class_weight             None
# criterion                gini
# max_depth                   3
# max_features             auto
# min_samples_leaf            9
# min_samples_split           3
# splitter                 best
# mean_test_score      0.820321
# Name: 2064, dtype: object
# =============================================================================

# =============================================================================
#      class_weight criterion  ...  splitter mean_test_score
# 2064         None      gini  ...      best        0.820321
# 3893         None   entropy  ...    random        0.811221
# 3244         None   entropy  ...      best        0.809948
# 2036         None      gini  ...      best        0.806027
# 3074         None   entropy  ...      best        0.805925
#           ...       ...  ...       ...             ...
# 131      balanced      gini  ...    random        0.515287
# 969      balanced      gini  ...    random        0.509770
# 1157     balanced   entropy  ...    random        0.509643
# 2003     balanced   entropy  ...    random        0.509456
# 1029     balanced   entropy  ...    random        0.505908
# =============================================================================

















