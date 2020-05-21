# -*- coding: utf-8 -*-
"""

XGBoost regression tree

"""

from xgboost import XGBClassifier , XGBRegressor
from xgboost import plot_importance

from sklearn.datasets import load_boston # cluster dataset create
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error , r2_score # model 평가

# 1. dataset load
boston = load_boston()
x_names = boston.feature_names

X , y = load_boston( return_X_y = True )
X.shape
y.shape

# dependent y is continous value and not normalize

# 2. data split
x_train , x_test , y_train , y_test = train_test_split(X , y ,test_size = 0.3)
xgb = XGBRegressor()
model = xgb.fit( x_train , y_train)
model

# 4. 중요 변수 시각화
fscore = model.get_booster().get_fscore()
fscore

x_names[0]
x_names[5]

plot_importance(model)
plt.show()

# 5. model 평가
y_pred = model.predict(x_test)
mse = mean_squared_error( y_test,y_pred)
mse
score = r2_score(y_test,y_pred)
score

import pandas as pd
tmp=pd.DataFrame(X)
tmp.corr()[0]












