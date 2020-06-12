# -*- coding: utf-8 -*-

'''
    - 변수 정의와 초기화
    - 상수 vs 변수
    - 상수 : 초기화 및 수정 불가
    - 변수 : 초기화 필요 및 수정 가능    
'''
import tensorflow.compat.v1 as tf # tensorflow 1.x

tf.disable_v2_behavior()

''' 프로그램 정의 영역 '''
# 상수 정의
x = tf.constant([1.5 , 2.5 , 3.5] , name = 'x') # 1차원

# 변수 정의
y = tf.Variable([1.0 , 2.0 , 3.0 ] , name = 'y') # 1차원 , 수정 가능

# 식 정의
mul = x * y # 상수 * 변수

# graph = node(연산자) + edge(data x, y)
# tensor = 데이터의 자료구조(scala , vector , matrix , array , n-array)

sess = tf.Session()
# 변수 초기화
init = tf.global_variables_initializer()

''' 프로그램 실행 영역 '''
print("x=", sess.run(x))
sess.run(init)
print("y=", sess.run(y))

#식 할당
mul_re = sess.run(mul)
print("mul=",mul_re) # [ 1.5  5.  10.5]
type(mul_re) # numpy.ndarray

mul_re.sum()

sess.close()

















