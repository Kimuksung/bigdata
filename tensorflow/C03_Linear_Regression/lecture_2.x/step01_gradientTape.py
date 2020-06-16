# -*- coding: utf-8 -*-
"""
step01_gradientTape.py

1. 미분(gradient)계수 자동 계산   
 - u자 곡선에서 접선의 기울기
 - tf.GradientTape : 미분계수 자동 계산 클래스 

2. low level API vs High level API
    - low level api : model , layer 사용자가 직접 작성 어렵다 -> code 어려움
    - High level api : model , layer 작성 쉽다 -> code 쉬움

"""

import tensorflow as tf
tf.executing_eagerly() # 즉시 실행 test : ver2.x 사용중 

######################################
# 미분(gradient)계수 자동 계산
######################################

# 1. input/output 변수 정의 
inputs = tf.Variable([1.0]) # x변수 
#outputs = tf.Variable([1.25]) # y변수
#outputs = tf.Variable([1.9]) # y변수
outputs = tf.Variable([2.8]) # y변수
print("outputs =", outputs.numpy())   

# 2. model : 예측치
def model(inputs) :    
    y_pred = inputs * 1.0 + 0.5 # 회귀방정식    
    print("y_pred =", y_pred.numpy()) 
    return y_pred  
 
# 2. 손실 함수
def loss(model, inputs, outputs):
  err = model(inputs) - outputs
  return tf.reduce_mean(tf.square(err)) # MSE

# 3. 미분계수(기울기) 계산  
with tf.GradientTape() as tape:
    loss_value = loss(model, inputs, outputs) # 손실함수 호출  
    print("손실값 =", loss_value.numpy())
    grad = tape.gradient(loss_value, inputs, outputs) 
    print("미분계수 =", grad.numpy())  

# =============================================================================
# 1차
# =============================================================================
# outputs = [1.25]
# y_pred = [1.5]
# 손실값 = 0.0625
# 미분계수 = [0.625]
# =============================================================================
# 2차
# =============================================================================
# outputs = [1.9]
# y_pred = [1.5]
# 손실값 = 0.15999998
# 미분계수 = [-1.5199999]
# =============================================================================
# 3차
# =============================================================================
# outputs = [2.8]
# y_pred = [1.5]
# 손실값 = 1.6899998
# 미분계수 = [-7.2799997]
# =============================================================================
