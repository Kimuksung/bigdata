# -*- coding: utf-8 -*-
"""
Decision Tree Model
    - important variable 선정 기준 : GINI , Entropy
    - GINI : 불확실성을 개선하는데 기여하는 척도
    - Entropy : 불확실성을 나타내는 지수 값


"""

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris , load_wine
from sklearn.tree import DecisionTreeClassifier ,export_graphviz
from sklearn.metrics import accuracy_score , confusion_matrix

# visualization
from sklearn.tree.export import export_text 
from sklearn import tree

iris = load_iris()
iris.target_names

x = iris.data
y = iris.target

x.shape

x_train , x_test , y_train , y_test = train_test_split(x,y ,test_size= 0.3)

dtc = DecisionTreeClassifier(criterion = "gini" , random_state = 123 , max_depth=3)

model = dtc.fit( x_train , y_train)

names = iris.feature_names
names
tree.plot_tree(model)
print(export_text(model , feature_names = names))

'''
|--- petal length (cm) <= 2.45
|   |--- class: 0
|--- petal length (cm) >  2.45
|   |--- petal length (cm) <= 4.75
|   |   |--- sepal length (cm) <= 4.95
|   |   |   |--- class: 2
|   |   |--- sepal length (cm) >  4.95
|   |   |   |--- class: 1
|   |--- petal length (cm) >  4.75
|   |   |--- petal width (cm) <= 1.75
|   |   |   |--- class: 2
|   |   |--- petal width (cm) >  1.75
|   |   |   |--- class: 2
'''

y_pred = model.predict(x_test)
y_true = y_test
accuracy_score(y_true , y_pred)
# 0.9111111111111111

confusion_matrix(y_true , y_pred)
'''
array([[14,  0,  0],
       [ 0, 15,  4],
       [ 0,  0, 12]], dtype=int64)
'''

dtc2 = DecisionTreeClassifier(criterion = "entropy" , random_state = 123 , max_depth=2)
model2 = dtc2.fit( x_train , y_train)
tree.plot_tree(model2)

y_pred2 = model2.predict(x_test)
y_true = y_test
accuracy_score(y_true , y_pred2)
# 0.9777777777777777
confusion_matrix(y_true , y_pred2)


##################################
# Model Overfitting
##################################

wine = load_wine()
X = wine.data
y = wine.target

x_train , x_test , y_train , y_test = train_test_split(X,y ,test_size= 0.3 ,random_state =123)

dt = DecisionTreeClassifier(max_depth = 3) # default
model = dt.fit(x_train, y_train)

model.score(x_train , y_train)
model.score(x_test , y_test)

tree.plot_tree(model) # max_depth = 6

# if max_depth is 3 train acc low, but test acc high
# if max depth is 6 train acc high , but test acc low
# so we need to find approximate max_depth

x_name = wine.feature_names
export_graphviz(model , out_file = "DT_tree_graph.dot" , feature_names = x_name , max_depth =3 ,
                class_names = True)







