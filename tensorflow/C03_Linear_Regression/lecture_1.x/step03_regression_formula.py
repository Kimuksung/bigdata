# -*- coding: utf-8 -*-
"""

단순 선형 회귀: X(1) -> Y
    - y_pred = X *a + b
    - err = (Y - y_pred)
    - loss function(cost function) = 실제 정답과 예측치 간의 오차 반환
        => function(Y , y_pred) : MSE
    
"""

import tensorflow as tf

# X , Y
X = tf.constant(6.5)
Y = tf.constant(5.2)

# a, b
a = tf.Variable(0.5)
b = tf.Variable(1.5)

def linear_model(X): 
    y_pred = tf.math.multiply(X ,a) + b # 회귀 방정식
    return y_pred

def model_err( X , Y) :
    y_pred = linear_model(X)
    err = Y - y_pred
    return err

# loss function : 정답 , 예측치 -> 오차 반환(MSE)
def loss_function(X , Y):
    err = model_err(X,Y)
    loss = tf.reduce_mean(tf.square(err))
    return loss

'''
오차 : MSE
Error : 정답 - 예측치
sqaure : 부호( + ) , 패널티
Mean : 전체 관측치의 오차 평균
'''

print("a = {} , b={}".format(a.numpy(), b.numpy()))
print("predict : {}".format(linear_model(X)))
print("model error : {}".format(model_err(X, Y)))
print("loss function : {}".format(loss_function( X, Y ).numpy()))
print("-"*20)

# 2차식 a = 0.6 b=1.2
a.assign(0.6)
b.assign(1.2)

print("a = {} , b={}".format(a.numpy(), b.numpy()))
print("predict : {}".format(linear_model(X)))
print("model error : {}".format(model_err(X, Y)))
print("loss function : {}".format(loss_function( X, Y ).numpy()))

'''

[키워드 정리]
최적화된 model : 최적의 기울기와 절편 -> 손실이 0에 수렴
딥러닝 최적화 알고리즘 : GD , Adam -> 최적의 기울기와 절편 수정 역할

'''












