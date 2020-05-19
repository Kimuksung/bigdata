# -*- coding: utf-8 -*-
"""

NB vs SVM : 희소 행렬( 고차원 )
    - 가중치 적용 : Tfidf     
"""

from sklearn.naive_bayes import MultinomialNB # NB model
from sklearn.svm import SVC # SVM model
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import accuracy_score , confusion_matrix 
import numpy as np

# 1. dataset pickle load
x_train , x_test , y_train , y_test = np.load("C:/ITWILL/4_Python-II/workspace/chap07_textmining/data/spam_data.npy" ,allow_pickle = True)

x_train.shape
x_test.shape

y_train = np.array(y_train)
y_test = np.array(y_test)
y_train.shape
y_test.shape

# 2. NBmodel
nb = MultinomialNB()
model = nb.fit( x_train , y_train)

y_pred = model.predict( x_test)
y_true = y_test

accuracy_score(y_true , y_pred)
confusion_matrix(y_true , y_pred)
'''
array([[1450,    0],
       [  39,  184]], dtype=int64)'''
184 / (184 + 39) # 0.8251121076233184

# 3. SVM model 속도는 NB가 더 빠르다.
svc = SVC(gamma = 'auto') # 비 선형
model_svc = svc.fit(x_train , y_train)
y_pred2 = model_svc.predict(x_test)
y_true2 = y_test

accuracy_score(y_true2 , y_pred2)
# 0.8667065152420801

confusion_matrix(y_true2 , y_pred2)
'''
array([[1450,    0],
       [ 223,    0]], dtype=int64)
'''
svc = SVC(gamma = 'auto' , kernel ='linear') # 비 선형
model_svc = svc.fit(x_train , y_train)
y_pred2 = model_svc.predict(x_test)
y_true2 = y_test

accuracy_score(y_true2 , y_pred2)
# 0.9832635983263598

confusion_matrix(y_true2 , y_pred2)
'''
array([[1449,    1],
       [  27,  196]], dtype=int64)
'''



















