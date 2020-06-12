# -*- coding: utf-8 -*-
"""

    - csv(pandas) -> tensorflow variable

"""

import pandas as pd
from sklearn.model_selection import  train_test_split # data split

import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() # ver 2.x 사용안함 

iris = pd.read_csv("C:/ITWILL/6_Tensorflow/data/iris.csv")
iris.info()

# 공급 data 생성
cols = list(iris.columns)
x_data = iris[cols[:4]]
y_data = iris[cols[-1]]

x_data.shape
y_data.shape

# x , y 변수 정의 : tensorflow 변수 정의
X = tf.placeholder(dtype = tf.float32 , shape = [ None , 4])
Y = tf.placeholder(dtype = tf.string , shape = [None])

# train test split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.3)
x_train.shape
x_test.shape

# session object : data 공급 -> 변수
with tf.Session() as sess:
    # train set
    train_feed_data = { X : x_train , Y : y_train}
    X_val , Y_val = sess.run( [X,Y] , feed_dict = train_feed_data)
    print(Y_val)
    print(X_val)
    
    # test set
    test_feed_data = { X : x_test , Y : y_test}
    X_val2 , Y_val2 = sess.run( [X,Y] , feed_dict = test_feed_data)
    print(Y_val2)
    print(X_val2)
    
    print(Y_val2.shape)
    print(type(Y_val2))
    
    # numpy -> pandas
    X_df = pd.DataFrame(X_val2 , columns = ['a','b','c','d'])
    print(X_df.info())
    X_df.mean()
    
    Y_ser = pd.Series(Y_val2)
    print(Y_ser.value_counts())
    
    
    





