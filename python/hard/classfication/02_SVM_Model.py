# -*- coding: utf-8 -*-
"""
SVM model
    - 선형 SVM vs 비선형 SVM
    - Hyper Parameter ( kernel , C , gamma)
    
"""

import pandas as pd #csv file read
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC # modeling
from sklearn.metrics import accuracy_score , confusion_matrix , f1_score  # model 평가 하기위해

iris = pd.read_csv("iris.csv")
iris.info()

cols = list(iris.columns)
x = cols[:-1]
y = cols[-1]

train , test = train_test_split(iris , test_size = 0.4 , random_state = 123 )

#model 생성
svc = SVC(gamma = 'auto') # 비선형 SVM model
# default C = 1.0 , kernel ='rbf'

svc2 = SVC(C = 1.0 , kernel = 'linear') # 선형 SVM model

model = svc.fit( train[x] , train[y])
model2 = svc2.fit( train[x] , train[y])

y_pred = model.predict( test[x])
y_true = test[y]

y_pred2 = model2.predict( test[x])
y_true2 = test[y]

acc = accuracy_score(y_true ,y_pred)
acc # 비선형 0.9666666666666667
 
acc = accuracy_score(y_true2 ,y_pred2)
acc # 선형 0.9666666666666667

############################################
# 최적의 값을 찾는법
# Grid Search
# Hyper Parameter ( kernel , C , gamma)
############################################

# C , gamma
params = [0.001 , 0.01, 0.1 , 1 ,10, 100] # 10^-3 ~ 10^2
kernel = ["rbf" , "linear"]

best_score = 0 
best_parameter = {}

for k in kernel :
    for gamma in params :
        for C in params:
            tmp = SVC( C = C , gamma = gamma , kernel=k)
            model = tmp.fit(train[x] , train[y])
            score = model.score(test[x], test[y])            
            
            if best_score < score:
                best_score = score
                best_parameter = {'kernel' : k , 'gamma':gamma , 'C' : C}
                
print(best_parameter)
best_score
























