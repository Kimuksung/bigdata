# -*- coding: utf-8 -*-
"""

    - Tensorflow 2.0 특징
        3. tf.function 함수 장식자(데코레이터)
            - 여러 함수들을 포함하는 main function

"""

import tensorflow as tf

# model 생성 함수
def linear_model(x):
    return x * 2 + 0.2 # linear

def model_err(y , y_pred):
    return y - y_pred # error

# model 평가 함수 : main function
@tf.function
def model_evaluation( x, y):
    y_pred = linear_model(x) #function call
    err = model_err( y , y_pred ) #function call
    return tf.reduce_mean(tf.square(err)) # mse

# x , y data 생성
X = tf.constant([1,2,3] , dtype = tf.float32 )
Y = tf.constant([2,4,6] , dtype = tf.float32 )

MSE = model_evaluation( X , Y)
print(MSE)

































