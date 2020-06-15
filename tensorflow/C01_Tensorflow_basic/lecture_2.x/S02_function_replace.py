# -*- coding: utf-8 -*-
"""

    - TensorFlow 2.0 특징
    2. 세션 대신 함수
        - ver 2.0 : 함수 사용 권장
        - API 정리 : tf.placeholder() 삭제 : 함수 인수 대체
"""
import tensorflow as tf # ver 2.0


''' version up '''
'''
a = tf.placeholder( dtype = tf.float32 ) # shape 생략 : 가변형
b = tf.placeholder( dtype = tf.float32 ) # shape 생략 : 가변형

c = tf.placeholder( dtype = tf.float32 , shape = [5] ) # 고정형 1d
d = tf.placeholder( dtype = tf.float32 , shape = [None , 3] ) # 고정형 2d , None -> 가변형

c_data = tf.random_uniform([5])

# 식 정의
mul = tf.multiply(a , b)

add = tf.add(mul , 10)

c_cal = c * 0.5 # 1d * 0d = 1d
'''

def mul_fn(a,b):
    return tf.multiply(a,b)

def add_fn(mul):
    return tf.add(mul,10)

def c_cala_fn(c):
    return c * 0.5

# data 생성
a_data = [1.0 , 2.5 , 3.5]
b_data =[2.0,3.0 , 4.0]

mul_re = mul_fn(a_data,b_data)
print("mul =" , mul_re.numpy())
print("add =" , add_fn(mul_re))
print("")
c_data = tf.random.uniform(shape = [3,4] , minval = 0 , maxval =1)
print(c_data)
print("")
print("c_cala func : " , c_cala_fn(c_data))



























