# -*- coding: utf-8 -*-
"""

Tensorflow 변수 유형
    1. 초기값을 갖는 변수 : Fetch 방식
        tf.Variable(초기값)
    
    2. 초기값이 없는 변수 : Feed 방식
        변수 = tf.Placeholder(dtype , shape)
        
"""

import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() # ver 2.x 사용안함 

# 상수 정의
x = tf.constant(100.0)
y = tf.constant(50.0)

# 식 정의
add = tf.add(x,y)

# 변수 정의
var1 = tf.Variable(add) # Fetch 방식
var2 = tf.placeholder(dtype = tf.float32) # Feed 방식 : 초기값 x

# 변수 참조하는 식
mul = tf.multiply(x, var1)
mul2 = tf.multiply(x , var2)

with tf.Session() as sess :
    print("add= ", sess.run(add))
    sess.run( tf.global_variables_initializer()) # 변수 초기화
    print("var1 = " , sess.run(var1))
    print("var2 = " , sess.run(var2, feed_dict = {var2 : 150} )) # data 공급
    
    #mul_re = sess.run(mul)
    print("mul = " , sess.run(mul))
    
    
    # feed 방식의 연산 수행
    print("mul2 = " , sess.run(mul2 , feed_dict ={var2:180 } ))
    print("mul2 = " , sess.run(mul2 , feed_dict ={var2: [1.4,2.4] } ))
    














