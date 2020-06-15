# -*- coding: utf-8 -*-
"""

    - X(1) -> Y
    - loss function
    - model optimizer algorithm : gradientDescentOptimizer , Adam
        => 모델 학습 : loss value 0 에 수렴하도록
        
"""

# version 1.x
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import numpy as np
print(tf.__version__)

# X, Y data 정의
x_data = np.array([1,2,3])
y_data = np.array([2,4,6])

X = tf.placeholder(dtype = tf.float32 , shape = [None])
Y = tf.placeholder(dtype = tf.float32 , shape = [None])

# a , b 정의
a = tf.Variable(tf.random_normal([1]))
b = tf.Variable(tf.random_normal([1]))

# 식 정의
model =  tf.multiply(X , a) + b #회귀 방정식

# 오차
err = Y - model

# loss function
loss = tf.reduce_mean(tf.square(err))

# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.1) # 학습률
train = optimizer.minimize(loss) # 손실 최소화 : 최적의 기울기 , 절편 수정


init = tf.global_variables_initializer()
# 반복 학습
with tf.Session() as sess:
    sess.run(init)
    a_val , b_val = sess.run([a,b])
    print("first time")
    print( "a = {} , b = {}".format(a_val , b_val))
    print()
    feed_data = { X : x_data , Y : y_data}
    
    for step in range(50):
        _, loss_val = sess.run([train , loss] , feed_dict = feed_data)
        print("step = " , (step+1), "loss =" , loss_val)
        a_val , b_val = sess.run([a,b])
        print( "a = {} , b = {}".format(a_val , b_val))
        print()
        










