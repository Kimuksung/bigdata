# -*- coding: utf-8 -*-
"""

- iris - 
X variable : 2~4 column
Y variable : 1 column

optimizer = Adam

"""

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 1. 공급 data 생성
iris = pd.read_csv("C:/ITWILL/6_Tensorflow/data/iris.csv")

cols = list(iris.columns)
x_data = iris[cols[1:4]]
y_data = iris[cols[0]]

x_train , x_test , y_train , y_test= train_test_split(x_data , y_data , test_size = 0.3)

# 2. X , Y 변수 정의
X = tf.placeholder(dtype = tf.float32 , shape = [None,3]) 
Y = tf.placeholder(dtype = tf.float32 , shape = [None])

# a,b 
a = tf.Variable(tf.random_normal(shape = [3 , 1 ])) 
b= tf.Variable(tf.random_normal(shape = [1]))

# model 생성
model = tf.matmul(X , a) + b
loss = tf.reduce_mean(tf.square(Y- model))

optimizer = tf.train.AdamOptimizer(0.1)
train = optimizer.minimize(loss)

# model 학습 : model 최적화
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    feed_data = { X : x_train , Y : y_train }
    for step in range(100):
        _, loss_val = sess.run([train , loss] , feed_dict = feed_data)
        print("step ={} , loss = {} \n".format(step+1 , loss_val) )
        a_val , b_val = sess.run([a,b])
        print( "a = {} , b = {}".format(a_val , b_val))
        print()
    #model 최적화
    a_up , b_up = sess.run([a,b])
    print(a_up , b_up)
    
    feed_data_test = {X : x_test , Y : y_test }
    
    y_true = sess.run( Y , feed_dict = feed_data_test)
    y_pred = sess.run(model , feed_dict = feed_data_test)

    mse = mean_squared_error(y_true , y_pred)
    print("mse :" , mse)


# =============================================================================
# 학습률 0.5
# 100회 반복 학습
# mse = 0.6234749
# =============================================================================
# 학습률 0.1
# 100회 반복 학습
# mse = 0.4892227
# =============================================================================
# 학습률 0.1
# 200회 반복 학습
# mse = 0.6103281
# =============================================================================
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    