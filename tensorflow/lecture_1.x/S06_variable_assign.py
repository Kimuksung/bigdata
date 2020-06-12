# -*- coding: utf-8 -*-
"""

    - 난수 상수 생성 함수 : 정규 분포 난수 / 균등 분포 난수
    tf.Variable(난수 상수) -> 변수 값 수정
    
    
"""
import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() # ver 2.x 사용안함 

# 난수
num = tf.constant(10.0)

# 변수
var = tf.Variable( num + 20.0) # scala
print("var = " , var) # <tf.Variable 'Variable_20:0' shape=() dtype=float32_ref>

# 1 차원 변수
var1d = tf.Variable(tf.random_normal([3])) # 1차원 : 3개의 1차원
print("var1d = " , var1d) # <tf.Variable 'Variable_22:0' shape=(3,) dtype=float32_ref>

# 2 차원 변수
var2d = tf.Variable(tf.random_uniform([3 , 2])) # 2차원 : [r,c]
print("var2d = " , var2d) # <tf.Variable 'Variable_25:0' shape=(3, 2) dtype=float32_ref>

# 3 차원 변수
var3d = tf.Variable(tf.random_normal([3,2,4])) # 3차원 : [s, row , col]
print("var3d = " , var3d) # <tf.Variable 'Variable_41:0' shape=(3, 2, 4) dtype=float32_ref>

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run( init ) # 변수 초기화
    
    print("var = " , sess.run(var))
    print("var1d = " ,sess.run(var1d))
    print("var2d = " , sess.run(var2d))

    # variable 수정
    var1d_data = [ 0.1 , 0.2 , 0.3]
    
    print("var1d assign : ", sess.run(var1d.assign(var1d_data)))
    print("assignadd" , sess.run(var1d.assign_add(var1d_data)))

    print("var3d : \n", sess.run(var3d))
    var3d_re = sess.run(var3d)
    
    #print("first" , var3d_re[0])
    #print("first + first" , var3d_re[0 , 0 ])
    #print("second" , var3d_re[1])
    #print("third" , var3d_re[2])

    # 24 개 균등 분포 난수 var3d 변수 값 수정
    sess.run(var3d.assign(tf.random_uniform([3,2,4])))
    print("change var3d : \n", sess.run(var3d))

    








