'''

Dataset class
    - Dataset으로 부터 사용가능한 데이터를 메모리에 로딩 기능
    - batch size 지정

'''

import tensorflow as tf
from tensorflow.python.data import Dataset

# member 
dir(Dataset)

'''
batch
from_tensor_slices
shuffle
'''

# 1. from_tensor_slices() : input tensor로 부터 slice 생성
# ex) MNIST(60000 , 28 , 28 ) -> 60000개 image를 각각 1개씩 slice

# 1) x,y
x = tf.random.normal([5,2])
y = tf.random.normal([5])

# 2) Dataset : 5개 slice
train_ds = Dataset.from_tensor_slices(( x , y ))
train_ds #  ((2,), ()), types: (tf.float32, tf.float32)

# 5개 관측치 -> 5개 slice
for train_x , train_y in train_ds:
    print("train_x: {} , train_y: {}".format(train_x , train_y))
'''
train_x: [-0.45244557  0.53960514] , train_y: -1.1737618446350098
train_x: [-0.422079    0.25540128] , train_y: 1.6923723220825195
train_x: [-0.11567031 -0.78749776] , train_y: 0.032122381031513214
train_x: [-0.27383578  0.3255406 ] , train_y: 0.20611800253391266
train_x: [-0.21172862 -1.3300066 ] , train_y: 1.3272353410720825
'''

# 2. from_tensor_slices((x,y)).shuffle(buffer size).batch(size)

'''
shuffle(buffer size) : tensor 행 단위 shuffling
    - buffer size : selected data size
batch : model 에 1회 공급할 크기

ex) 60,000 (mnist)-> shuffle(10000).batch(100)
    firstr slice data : 10000 data shuffling -> for 100 extract
    second slice data : next 10000data shuffling -> for 100 extract
    
'''
print()
# 1) x,y
x2 = tf.random.normal([5,2])
y2 = tf.random.normal([5])

# 2) Dataset : 5개 slice
train_ds2 = Dataset.from_tensor_slices(( x2 , y2 )).shuffle(5).batch(2)
train_ds2 #  ((2,), ()), types: (tf.float32, tf.float32)

# 3) 3 slice -> 1 slice
for train_x , train_y in train_ds2:
    print("train_x: {} , train_y: {}".format(train_x , train_y))


# 3. keras dataset 적용
from tensorflow.keras.datasets.cifar10 import load_data

# 1. dataset load
(x_train , y_train ) , (x_val , y_val) = load_data()
x_train.shape # (50000, 32, 32, 3)
y_train.shape # (50000, 1)

import matplotlib.pyplot as plt
plt.imshow(x_train[0])
plt.show()

# batchsize = 100
train_ds = Dataset.from_tensor_slices(( x_train , y_train )).shuffle(10000).batch(100)

cnt = 0
for img_x , label_x in train_ds:
    print("image ={} , label ={}".format(img_x.shape , label_x.shape))
    cnt+=1
    
print(cnt)
#epochs = itersize(500) * batch size(100)
# val set batch size = 100 image

train_ds = Dataset.from_tensor_slices(( x_val , y_val )).shuffle(1000).batch(100)

cnt = 0
for img_x , label_x in train_ds:
    print("image ={} , label ={}".format(img_x.shape , label_x.shape))
    cnt+=1
    
print(cnt)

# MNIST -> train_ds , val_ds
    #train_ds : shuffle = 10,000 , batch size = 32
    #val_ds : batch size =32

from tensorflow.keras.datasets.mnist import load_data
(x_train , y_train ) , (x_val , y_val) = load_data()
x_train.shape # (60000, 28, 28)
train_ds = Dataset.from_tensor_slices(( x_train , y_train )).shuffle(10000).batch(32)
val_ds = Dataset.from_tensor_slices(( x_val , y_val )).batch(100)

import numpy as np
np.matrix([[0.0]]).shape

cnt = 0
for img_x , label_x in train_ds:
    print("image ={} , label ={}".format(img_x.shape , label_x.shape))
    cnt+=1