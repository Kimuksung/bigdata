'''
선형대수 연산 함수
 tf.transpose : 전치행렬   
 tf.diag : 대각행렬 -> tf.linalg.diag(x)  
 tf.matrix_determinant : 정방행렬의 행렬식 -> tf.linalg.det(x)
 tf.matrix_inverse : 정방행렬의 역행렬 -> tf.linalg.inv(x)
 tf.matmul : 두 텐서의 행렬곱 -> tf.linalg.matmul(x, y)
 tf.eye : tf.linalg.eye (one-hot encoding)
'''

import tensorflow as tf
import numpy as np

# 정방행렬 데이터 생성 
x = np.random.rand(2, 2) # 지정한 shape에 따라서  0~1 난수 
y = np.random.rand(2, 2) # 지정한 shape에 따라서  0~1 난수 

tran = tf.transpose(x) # 전치행렬
dia = tf.linalg.diag(x) # 대각행렬 
mat_deter = tf.linalg.det(x) # 정방행렬의 행렬식  
mat_inver = tf.linalg.inv(x) # 정방행렬의 역행렬
mat = tf.linalg.matmul(x, y) # 행렬곱 반환 
eye = tf.linalg.eye(3) # 단위 행렬

print(x)
print(tran)  
print(dia) 
print("-"*20)
print(mat_deter)
print(mat_inver)
print(mat)
print(eye)

# 단위 행렬 -> one hot encoding
import  numpy as np
a = [ 0 , 1, 2 ]
encoding = np.eye(len(a))[a]
print(encoding)

# =============================================================================
# multiply vs matmul - input의 갯수에 따라 나누어진다.
# tf.multiply : broadcast
# - X * a
# tf.matmul : 행렬곱
# - X1 * a1 + X2 * a2
# 
# =============================================================================









