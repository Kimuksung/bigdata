# -*- coding: utf-8 -*-
"""

    - 초기값이 없는 변수
        tf.placeholder(dtype , shape )
        dtype = 자료형 ( tf.float32 , tf.int32 , tf.string )
        shape = 자료 구조( [ n ] : 1차원 , [r,c ] : 2차원  , 생략 : 공급 data 결정 )

"""

import tensorflow.compat.v1 as tf # ver 1.x
tf.disable_v2_behavior() # ver 2.x 사용안함 

a = tf.placeholder( dtype = tf.float32 ) # shape 생략 : 가변형
b = tf.placeholder( dtype = tf.float32 ) # shape 생략 : 가변형

c = tf.placeholder( dtype = tf.float32 , shape = [5] ) # 고정형 1d
d = tf.placeholder( dtype = tf.float32 , shape = [None , 3] ) # 고정형 2d , None -> 가변형

c_data = tf.random_uniform([5])

# 식 정의
mul = tf.multiply(a , b)

add = tf.add(mul , 10)

c_cal = c * 0.5 # 1d * 0d = 1d

with tf.Session() as sess: 
    # 변수 초기화 생략
    print("mul : " , sess.run(mul , feed_dict= { a: 2.5 , b:3.5}))
    a_data = [1.0 , 2.0 , 3.5]
    b_data = [0.5 , 0.3 , 0.4]
    feed_data = { a : a_data , b : b_data}
    print("mul2 : " , sess.run(mul , feed_dict= feed_data))

    # 식 실행 : 식 참조
    print("add : " , sess.run(add , feed_dict = feed_data))
    
    c_data_re = sess.run(c_data)
    print("c_data_re :", c_data_re)
    print("c_data:",sess.run( c_cal , feed_dict = {c:c_data_re}))

    ''' 주의 사항 
    프로그램 정의 변수와 리턴 변수는 다르게 지정해야 한다
    '''





