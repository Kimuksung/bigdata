'''

- MNIST + CNN + nameScope + tensorboard

0. input layer : image( ? x 28 x 28 -> ?(-1) x 28 x 28 x 1)
1. Convolution layer1( Conv -> relu -> pool )
2. Convolution layer2( Conv -> relu -> pool )
3. Flatten layer : 3d [size , h , w , c] ->  1d [size , h*w*c]   // h*w*c = n
4. DNN hidden layer1 : [s , n ] * [ n * node ]
5. DNN output layer : [node , 10]

'''

import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.0 사용안함
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets.mnist import load_data # dataset load
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

tf.reset_default_graph() # tensorboard 초기화(안하면 전에것도 출)

# 1. image read 
(x_train, y_train), (x_test, y_test) = load_data()
print(x_train.shape) # (60000, 28, 28)
print(y_train.shape) # (60000,) : 10진수 

# 2. 실수형 변환 : int -> float32
x_train = x_train.astype('float32') 
x_test = x_test.astype('float32')

# 3. 정규화 
x_train = x_train / 255 # x_train = x_train / 255
x_test = x_test / 255

# first image 
img = x_train[0]
plt.imshow(img, cmap='gray') # 숫자 5  

# 4. input image reshape  
x_train = x_train.reshape(-1,28,28,1) #(size , h , w, color)
x_test = x_test.reshape(-1 , 28 , 28, 1)

# 5. y_data preprocssing : one-hot encoding
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# x , y variable 정의
x_img = tf.placeholder(tf.float32 , shape = [None,28,28,1])
Y = tf.placeholder(tf.float32 , shape = [None,10])

# 합성곱 계층 함수
def conv2d_func(img , Filter):
    return tf.nn.conv2d( input = img ,  filter = Filter , strides = [1,1,1,1] , padding = 'SAME')
    
def max_pool(X):
    return tf.nn.max_pool(X , ksize = [1,2,2,1] , strides = [1,2,2,1] , padding='SAME')

# 1. conv layer1
with tf.name_scope("Convolution1") as scope:
    Filter1 = tf.Variable(tf.random_normal([3,3,1,32]))
    #conv2 = tf.nn.conv2d( input = x_img ,  filter = Filter1 , strides = [1,1,1,1] , padding = 'SAME')
    conv2 = conv2d_func(x_img , Filter1)
    L1 =tf.nn.relu(conv2)
    #L1_out = tf.nn.max_pool(L1 , ksize = [1,2,2,1] , strides = [1,2,2,1] , padding='SAME')
    L1_out = max_pool(L1)
    print(L1_out) #Tensor("MaxPool_1:0", shape=(?, 14, 14, 32), dtype=float32)

# 2. conv layer2
with tf.name_scope("Convolution2") as scope:
    Filter2 = tf.Variable(tf.random_normal([3,3,32,64]))
    #conv2_l2 = tf.nn.conv2d( input = L1_out ,  filter = Filter2 , strides = [1,1,1,1] , padding = 'SAME')
    conv2_l2 = conv2d_func(L1_out , Filter2)
    L2 =tf.nn.relu(conv2_l2)
    #L2_out = tf.nn.max_pool(L2 , ksize = [1,2,2,1] , strides = [1,2,2,1] , padding='SAME')
    L2_out = max_pool(L2)
    print(L2_out) # Tensor("MaxPool_6:0", shape=(?, 7, 7, 64), dtype=float32)

# 3. flatten layer
with tf.name_scope("Flatten") as scope:
    n = 7 * 7 * 64 
    L3_Flat = tf.reshape(L2_out , [-1 , n])
    print(L3_Flat)

# 4. dnn layer

#Hyper parameters
lr = 0.01
epochs = 10 #전체 dataset 재사용 횟수
batch_size =100#1회 data 공급 횟수
iter_size = 600 #반복 횟수
input_size = n
hidden_nodes = 128 

# ============================================================================= 
# DNN network
# hidden1 nodes : 128
# hidden2 nodes : 64
# output nodes : 10
# =============================================================================


with tf.name_scope("DNN_hidden_layer") as scope:
# 5. softmax 알고리즘 
# (1) model
    # hidden layer1
    w1 = tf.Variable(tf.random_normal([ input_size , hidden_nodes]) , name = 'w1')
    b1 = tf.Variable(tf.random_normal([ hidden_nodes ]) , name='b1')
    hidden1_output = tf.nn.relu(tf.matmul( L3_Flat , w1) + b1)

with tf.name_scope("DNN_output_layer") as scope:
    # output layer 
    w2 = tf.Variable(tf.random_normal([ hidden_nodes , 10]) , name='w2')
    b2 = tf.Variable(tf.random_normal([ 10 ]), name='b2')

    model = tf.matmul(hidden1_output , w2) + b2                           
    softmax = tf.nn.softmax(model) 

    # (2) softmax
    softmax = tf.nn.softmax(model) # 활성함수 

with tf.name_scope("Loss_Function") as scope:
    # (3) loss function : Softmaxt + Cross Entorpy
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
            labels = Y, logits = model))

with tf.name_scope("Optimizers") as scope:
    # (4) optimizer 
    train = tf.train.AdamOptimizer(lr).minimize(loss)
    
with tf.name_scope("Prediction") as scope:
    # (5) encoding -> decoding 
    y_pred = tf.argmax(softmax, axis = 1)
    y_true = tf.argmax(Y, axis = 1)


# 6. model training
with tf.Session() as sess :
    sess.run(tf.global_variables_initializer()) # w, b 초기화 
    
    tf.summary.merge_all() # tensor collect
    writer = tf.summary.FileWriter("C:/ITWILL/6_Tensorflow/graph" , sess.graph)
    print("tensorboard visualization is completed")
    writer.close()  
    
    feed_data = {x_img : x_train , Y : y_train}
    
    for epoch in range(epochs) : 
        tot_loss = 0
        for step in range(iter_size):
            idx = np.random.choice( a = y_train.shape[0] ,size = batch_size , replace =False)
            feed_data = { x_img : x_train , Y : y_train}
            _, loss_val = sess.run([train , loss] , feed_dict = feed_data)
            
            tot_loss += loss_val
        #1epoch 종료
        avg_loss = tot_loss / iter_size
        print("epoch = {} , loss = {}".format(epoch, avg_loss))
        
    # model test 
    feed_data2 = {x_img : x_test, Y : y_test}
    y_pred_re = sess.run(y_pred, feed_dict = feed_data2)
    y_true_re = sess.run(y_true, feed_dict = feed_data2)
    
    
    acc = accuracy_score(y_true_re, y_pred_re)
    print("accuracy =", acc)













