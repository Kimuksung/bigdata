# -*- coding: utf-8 -*-
"""

Pipeline vs Grid Search
1. SVM model
2. Pipeline : model workflow ( dataset 전처리 -> model -> test)
3. Grid Search : model tuning(최적의 parameter를 찾는 과정)

"""

from sklearn.svm import SVC
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler #scaling
from sklearn.pipeline import Pipeline # model workflow
import numpy as np

# 1. SVM model
X, y = load_breast_cancer(return_X_y = True )
X.shape

# 열 평균
X.mean(axis=0)
X.min() # 0
X.max() # 4254.0

# X variable normalize
#X_nor = np.array(MinMaxScaler().fit(X))
#X_nor.mean(axis=0)

tmp = MinMaxScaler().fit_transform(X)
tmp.mean()
tmp.shape

scaler = MinMaxScaler().fit(X)
X_nor = scaler.transform(X)
X_nor.mean()

x_train , x_test , y_train , y_test = train_test_split(X_nor , y , test_size = 0.3 , random_state = 123 )

svc = SVC(gamma= 'auto')
model = svc.fit(x_train , y_train)

model.score(x_test , y_test) # 0.9590643274853801

# Pipeline : model workflow
# 1. pipeline step : [ (step1) , (step2) , ..]
pipe_svc = Pipeline([( 'scaler' , MinMaxScaler()) , ('svc' , SVC(gamma = 'auto'))])

# 2. pipeline model
model = pipe_svc.fit(x_train , y_train)

# 3. pipeline model test
model.score(x_test ,y_test)
# 0.9590643274853801



# 4. Greed Search
# pipeline -> grid search -> model tuning

from sklearn.model_selection import GridSearchCV

# 1) params 설정
params = [ 0.001 , 0.01 , 0.1 , 1.0 , 10.0 ,100.0 , 1000.0]

params_grid = [
                {'svc__C' : params , 'svc__kernel' : ['linear']} ,
                {'svc__C' : params , 'svc__gamma' : params , 'svc__kernel' : ['rbf']}
               ] 

# 2) gridsearchcv object
pipe_svc = Pipeline([( 'scaler' , MinMaxScaler()) , ('svc' , SVC(gamma = 'auto'))])
gs = GridSearchCV(estimator = pipe_svc , param_grid = params_grid , scoring = 'accuracy', cv=10 )

model = gs.fit(x_train , y_train)
model.score(x_test , y_test )

model.best_params_
# {'svc__C': 1.0, 'svc__gamma': 1.0, 'svc__kernel': 'rbf'}














