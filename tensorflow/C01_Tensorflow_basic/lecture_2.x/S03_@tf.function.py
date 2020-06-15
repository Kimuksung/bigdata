# -*- coding: utf-8 -*-
"""

    - Tensorflow 2.0 특징
        3. tf.function 함수 장식자(데코레이터)
        이점
        - python code -> tensorflow code 변환(auto graph)
        - logic 처리 : 쉬운 코드 대체
        - 속도 향상
        
"""

import tensorflow as tf

'''version up '''

'''
# 1. if문
x = tf.constant(10)

def true_fn():
    return tf.multiply(x , 10)

def false_fn():
    return tf.add(x , 10)

y = tf.cond( x > 100 ,true_fn , false_fn )

# 2. while문
i = tf.constant( 0 )
def cond(i):
    return tf.less(i , 100)

def body(i) :
    return tf.add(i,1)
 
loop = tf.while_loop( cond , body , (i,))
'''

@tf.function
def if_func(x):
    if x>100:
        y = x * 10
    else :
        y = x + 10
    return y

x = tf.constant(10)
print(if_func(x))

@tf.function
def while_func(i):
    while i < 100 :
        i += 1
    
    return i

i = tf.constant(0)
print(while_func(i))



















