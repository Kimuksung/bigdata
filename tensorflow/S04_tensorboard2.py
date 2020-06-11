# -*- coding: utf-8 -*-
"""

    -name scope : 영역별 tensorboard 시각화
        1) model 생성 - > model 오차 -> model 평가

"""

import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() # ver 2.x 사용안함 
tf.reset_default_graph()

# 상수 정의 : x , y , a ,b (linear)
X = tf.constant(5.0 , name = "x_data") # x
a = tf.constant(10.0 , name ="a")
b = tf.constant(4.45 , name = 'b')
y = tf.constant(55.0 , name = 'y_data')

# name_scope
with tf.name_scope("regress_model") as scope :
    model = ( X * a ) + b

with tf.name_scope("model_error") as scope:
    model_err = tf.subtract(y , model) # 부호 절대값

with tf.name_scope("Model_evaluation") as scope:
    square = tf.square(model_err)
    mse = tf.reduce_mean(square)

with tf.Session() as sess :
    tf.summary.merge_all() # tensor collect
    writer = tf.summary.FileWriter("C:/ITWILL/6_Tensorflow/graph" , sess.graph)
    writer.close()  
    print("X = " , sess.run(X))
    print("y = " , sess.run(y))
    print("y pred = " , sess.run(model))
    print("model error = " , sess.run(model_err))
    print("mse = " , sess.run(mse))
    











