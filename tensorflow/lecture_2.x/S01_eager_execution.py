# -*- coding: utf-8 -*-
"""

    - TensorFlow 2.0 feature
    1. 즉시 실행 환경  
        - session object 없이 즉시 실행 환경 ( auto graph)
        - python 실행 환경과 동일함
        - API 정리 : tf.global_variable_initialzer 삭제
    2. 

"""

import tensorflow as tf # ver 2.0
print(tf.__version__)

# 상수 정의
a = tf.constant([[1,2,3] , [1.0,2.5,3.5]]) # shape = [2,3]
print(a)
# =============================================================================
# tf.Tensor(
# [[1.  2.  3. ]
#  [1.  2.5 3.5]], shape=(2, 3), dtype=float32)
# =============================================================================
print(a.numpy())
# =============================================================================
# [[1.  2.  3. ]
#  [1.  2.5 3.5]]
# =============================================================================

# 식 정의
b = tf.add(a  , 0.5) # 즉시 실행
print(b.numpy())
# =============================================================================
# [[1.5 2.5 3.5]
#  [1.5 3.  4. ]]
# =============================================================================

# 변수 정의
x = tf.Variable([10,20,30])
y = tf.Variable([1,2,3])

mul = tf.multiply(x,y)
print(mul)
# [10 40 90]


''' python code -> tensorflow 즉시 실행 '''
x = [[2.0 , 3.0 ]] # shape = [1,2]
a = [[1.0] , [1.5]] # shape = [2,1]

# 행렬곱 연산
mat = tf.matmul( x , a)
print( "matrix multiply = {}".format(mat) )
# matrix multiply = [[6.5]]


'''즉시 실행 모드'''
# tf_variable_init -> version 2.0
print("")
print("version up")
print("")
# 상수 정의
x = tf.constant([1.5 , 2.5 , 3.5] , name = 'x') # 1차원

# 변수 정의
y = tf.Variable([1.0 , 2.0 , 3.0 ] , name = 'y') # 1차원 , 수정 가능

# 식 정의
mul = x * y # 상수 * 변수

print("x=", x)

print("y=",y)

#식 할당
print("mul=",mul.numpy()) 








