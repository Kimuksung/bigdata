# -*- coding: utf-8 -*-
"""

1. 즉시 실행 모드
2. 세션 대신 함수
3. 함수 장식자

"""

import pandas as pd
from sklearn.model_selection import  train_test_split # data split
import numpy as np 

import tensorflow as tf

iris = pd.read_csv("C:/ITWILL/6_Tensorflow/data/iris.csv")
iris.info()

@tf.function
def tt_split( iris ):

    
    x_train, x_test, y_train, y_test = np.array(train_test_split(x_data, y_data, test_size = 0.3))
    return x_train, x_test, y_train, y_test

x_train, x_test, y_train, y_test = tt_split( iris)

cols = iris.columns
x_data = iris[cols[:4]]
x_data=tf.constant( np.array(x_data))
y_data = iris[cols[-1]]
y_data=tf.constant( np.array(y_data))
type(np.array(x_data))















