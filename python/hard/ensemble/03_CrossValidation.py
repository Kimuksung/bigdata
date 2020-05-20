# -*- coding: utf-8 -*-
"""

교차 검정( Cross Validation )

"""

from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split , cross_validate
from sklearn.metrics import accuracy_score
# 1. dataset load
digit = load_digits()

X = digit.data
y = digit.target

X.shape # (1797, 64)
y

rf = RandomForestClassifier()
model = rf.fit(X,y)

pred = model.predict(X)
pred
pred2 = model.predict_proba(X)
pred2
# 확률 -> index(10 진수)
pred2_dit = pred2.argmax(axis=1)
pred2_dit

accuracy_score(y,pred) # 1.0

accuracy_score(y,pred2_dit) # 1.0

# 3. Cross Validation
score = cross_validate( model , X , y , scoring = 'accuracy' , cv = 5)
test_score = score['test_score'] #array([0.93055556, 0.91388889, 0.95821727, 0.95543175, 0.9275766 ])
test_score.mean() # 0.9371340142370783



























