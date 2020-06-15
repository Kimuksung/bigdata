'''
expand_dims
 - tensor에 축 단위로 차원을 추가하는 함수 
'''

import tensorflow as tf
const = tf.constant([1,2,3,4,5]) # 1차원 

print(const)
print(const.shape) # (5,)

d0 = tf.expand_dims(const, axis=0) # 행 축 2차원 
print(tf.shape(d0)) # [1 5]
print(d0) # [[1 2 3 4 5]], shape=(1, 5)
    
d1 = tf.expand_dims(const, axis=1) # 열 축 2차원 
print(tf.shape(d1)) # [5 1]
print(d1)
'''
[[1]
 [2]
 [3]
 [4]
 [5]], shape=(5, 1)
'''

# 행렬곱에서 차수 불일치 문제 해결
x_data = tf.constant([10 , 20 ]) 
x_data.get_shape()   
tf.expand_dims(x_data , axis = 0)

import numpy as np
tmp1 = np.array([10 , 20 ])
tmp1 = tmp1.reshape(1,2)

y_data =tf.constant( [[1,2,3] , [4,5,6]])
y_data.get_shape()

mat = tf.matmul(tf.expand_dims(x_data , axis = 0) , y_data)
mat
mat2 = tf.matmul(tmp1 , y_data)
mat2
