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

# balanced sampling(downsampling) + logistic
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score  , confusion_matrix

x_cols = plant1_balancedsample.columns[:2]
y_cols = plant1_balancedsample.columns[-1]

lr = LogisticRegression(C=0.001 , penalty ='l2')
#'C': 0.001, 'penalty': 'l2'
model = lr.fit(X = plant1_balancedsample[x_cols],y = plant1_balancedsample[y_cols])

model.score(plant1_balancedsample[x_cols] , plant1_balancedsample[y_cols] )

# 0.7979139504563233

plant1_sample = pd.concat([plant1_train_first_24_true , plant1_train_first_24_false])
y_pred = model.predict(plant1_sample[x_cols])
confusion_matrix(plant1_sample[y_cols], y_pred)
# =============================================================================
# array([[48605,  8528],
#        [   77,   190]]
# =============================================================================
print(classification_report(plant1_sample[y_cols], y_pred))

# =============================================================================
#              precision    recall  f1-score   support
# 
#          0.0       1.00      0.85      0.92     57133
#          1.0       0.02      0.72      0.04       267
# 
#     accuracy                           0.85     57400
#    macro avg       0.51      0.79      0.48     57400
# weighted avg       0.99      0.85      0.91     57400
# 
# =============================================================================

'''
# grid search
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import numpy as np
param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100],
              'penalty': ['l1', 'l2']}

grid_search = GridSearchCV(LogisticRegression(), param_grid, cv=5)

grid_search.fit(X = plant1_balancedsample[x_cols],y = plant1_balancedsample[y_cols])
grid_search.score(plant1_sample[x_cols], plant1_sample[y_cols])

best_score = 0

# iterataion
for r in ['l1', 'l2']:
    for C in [0.001, 0.01, 0.1, 1, 10, 100]:
        lm = LogisticRegression(penalty = r, C=C)
        scores = cross_val_score(lm, plant1_balancedsample[x_cols], plant1_balancedsample[y_cols], cv=5)
        score = np.mean(scores)
        if score > best_score:
            best_score = score
            best_parameters = {'C': C, 'penalty': r}

'C': 0.001, 'penalty': 'l2'
'''
















