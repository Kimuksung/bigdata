# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime , timedelta
plant1_train = pd.read_csv('plant1_train.csv')
plant2_train = pd.read_csv("plant2_train.csv")


plant1_train = plant1_train.drop('Unnamed: 0' , axis=1)
cols = ['Date' , 'loc1_tem', 'loc1_hum', 'loc1_coil_temp','loc2_tem', 'loc2_hum', 'loc2_coil_temp' , 'loc3_tem', 'loc3_hum', 'loc3_coil_temp', 'out_tem', 'out_hum', 'loc1' , 'loc2' , 'loc3']
plant1_train.columns = cols

#'''

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

# balanced sampling (downsampling)
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

lr = LogisticRegression()
model = lr.fit(X = plant1_balancedsample[x_cols],y = plant1_balancedsample[y_cols])

model.score(plant1_balancedsample[x_cols] , plant1_balancedsample[y_cols] )
# 0.7979139504563233
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

#grid search

#params = [0.001 , 0.01, 0.1 , 1 ,10, 100] # 10^-3 ~ 10^2
#kernel = ["poly"]

#best_score = 0 
#best_parameter = {}

#for k in kernel :
   # for gamma in params :
     #   for C in params:
     #       tmp = SVC( C = C , gamma = gamma , kernel=k)
    #        print(k , C )
   #         model = tmp.fit(X = plant1_balancedsample[x_cols],y = plant1_balancedsample[y_cols])
   #         score = model.score(plant1_balancedsample[x_cols] , plant1_balancedsample[y_cols])            
            
  #          if best_score < score:
 #               best_score = score
 #               best_parameter = {'kernel' : k , 'gamma':gamma , 'C' : C}
                
#print(best_parameter)
# {'kernel': 'rbf', 'gamma': 100, 'C': 10}
#best_score

plant1_sample = pd.concat([plant1_train_first_24_true , plant1_train_first_24_false])
y_pred = model.predict(plant1_sample[x_cols])
confusion_matrix(plant1_sample[y_cols], y_pred)


#array([[48754,  8379],
#       [   77,   190]], dtype=int64)


# balanced sampling(downsampling) + svm
from sklearn.svm import SVC

svc = SVC( kernel= 'rbf', gamma= 100, C= 10)

model = svc.fit( X = plant1_balancedsample[x_cols],y = plant1_balancedsample[y_cols] )
model.score(plant1_balancedsample[x_cols] , plant1_balancedsample[y_cols] )
#0.940026075619296 -> best paramter 0.9986962190352021

y_pred = model.predict(plant1_sample[x_cols])
confusion_matrix(plant1_sample[y_cols], y_pred)

print(classification_report(plant1_sample[y_cols], y_pred))

# =============================================================================
#               precision    recall  f1-score   support
# 
#          0.0       1.00      1.00      1.00     57133
#          1.0       0.50      1.00      0.67       267
# 
#     accuracy                           1.00     57400
#    macro avg       0.75      1.00      0.83     57400
# weighted avg       1.00      1.00      1.00     57400
# =============================================================================

#y_pred = model.predict(plant1_balancedsample[x_cols])
#confusion_matrix(plant1_sample[y_cols], y_pred)

#print(classification_report(plant1_balancedsample[y_cols], y_pred))

#array([[53525,  3608],
#       [   31,   236]], dtype=int64)

#-> best parameter  

#array([[56861,   272],
#       [    0,   267]], dtype=int64)


#grid search

#params = [0.001 , 0.01, 0.1 , 1 ,10, 100] # 10^-3 ~ 10^2
#kernel = ["poly"]

#best_score = 0 
#best_parameter = {}

#for k in kernel :
   # for gamma in params :
     #   for C in params:
     #       tmp = SVC( C = C , gamma = gamma , kernel=k)
    #        print(k , C )
   #         model = tmp.fit(X = plant1_balancedsample[x_cols],y = plant1_balancedsample[y_cols])
   #         score = model.score(plant1_balancedsample[x_cols] , plant1_balancedsample[y_cols])            
            
  #          if best_score < score:
 #               best_score = score
 #               best_parameter = {'kernel' : k , 'gamma':gamma , 'C' : C}
                
#print(best_parameter)
# {'kernel': 'rbf', 'gamma': 100, 'C': 10}
#best_score

# Decision Tree
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion = "gini", max_depth=2)
model = dtc.fit( X = plant1_balancedsample[x_cols],y = plant1_balancedsample[y_cols] )

y_pred = model.predict(plant1_sample[x_cols])
confusion_matrix(plant1_sample[y_cols], y_pred)
# =============================================================================
# array([[51518,  5615],
#        [   76,   191]], dtype=int64)
# =============================================================================
print(classification_report(plant1_sample[y_cols], y_pred))
# =============================================================================
#               precision    recall  f1-score   support
# 
#          0.0       1.00      0.90      0.95     57133
#          1.0       0.03      0.72      0.06       267
# 
#     accuracy                           0.90     57400
#    macro avg       0.52      0.81      0.51     57400
# weighted avg       0.99      0.90      0.94     57400
# =============================================================================

# Random Forest
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
model = rf.fit( X = plant1_balancedsample[x_cols],y = plant1_balancedsample[y_cols] )

y_pred = model.predict(plant1_sample[x_cols])
confusion_matrix(plant1_sample[y_cols], y_pred)
# =============================================================================
# array([[52278,  4855],
#        [    0,   267]], dtype=int64)
# =============================================================================
print(classification_report(plant1_sample[y_cols], y_pred))

# =============================================================================
#               precision    recall  f1-score   support
# 
#          0.0       1.00      0.92      0.96     57133
#          1.0       0.05      1.00      0.10       267
# 
#     accuracy                           0.92     57400
#    macro avg       0.53      0.96      0.53     57400
# weighted avg       1.00      0.92      0.95     57400
# =============================================================================



'''

# second에 svm loc1꺼 넣어서 해보자
plant1_train_second = plant1_train[['Date','loc2_tem', 'out_tem' , 'loc2_coil_temp','loc2_hum' ,'out_hum','loc2']]

date_trans = []
for i in range(0,len(plant1_train_second)):
    date_trans.append(datetime.strptime(plant1_train_second['Date'][i] , '%Y-%m-%d %H:%M'))

plant1_train_second['date_trans'] = date_trans
plant1_train_second

hour24 = []
for i in range(0,len(plant1_train_second)):
    tmp = datetime.strptime(plant1_train_second['Date'][i]  , '%Y-%m-%d %H:%M') + timedelta(days=1)
    tmp1 = datetime.strptime(plant1_train_second['Date'][i]  , '%Y-%m-%d %H:%M')
    if(len(plant1_train_second[plant1_train_second['date_trans']==tmp]) > 0 ):
        loc_24hour = plant1_train_second[plant1_train_second['date_trans']==tmp]
        print(plant1_train_second['Date'][i])
        print(loc_24hour['Date'])
        print("this", float(loc_24hour['loc2'].values))
        print("-"*10)
        hour24.append(float(loc_24hour['loc2'].values))
    else:
        hour24.append(float('NaN'))

plant1_train_second['24hourloc'] = hour24
plant1_train_second

plant1_train_second_24 = plant1_train_second.dropna(axis=0)

# balanced sampling (downsampling)
plant1_train_second_24_true = plant1_train_second_24[plant1_train_second_24['24hourloc']==1]
plant1_train_second_24_false = plant1_train_second_24[plant1_train_second_24['24hourloc']==0]

plant1_train_second_24_true = plant1_train_second_24_true.drop(['Date', 'loc2_tem', 'out_tem', 'out_hum','loc2', 'date_trans'], axis=1)
plant1_train_second_24_false = plant1_train_second_24_false.drop(['Date', 'loc2_tem', 'out_tem', 'out_hum','loc2', 'date_trans'], axis=1)


plant1_loc2_balancedsample = pd.concat([plant1_train_second_24_true, plant1_train_second_24_false])
x_cols = ['loc2_coil_temp', 'loc2_hum']

model.score(plant1_loc2_balancedsample[x_cols] , plant1_loc2_balancedsample[y_cols] )
y_pred = model.predict(plant1_loc2_balancedsample[x_cols])
confusion_matrix(plant1_loc2_balancedsample[y_cols], y_pred)

from sklearn.metrics import classification_report
print(classification_report(plant1_loc2_balancedsample[y_cols], y_pred))
'''
