"""

DNN model
    - hidden layer : relu function
    - output layer : Softmax activation function
    - hidden1 layer classifier node =12
    - hidden2 layer classifier node = 6
    - data set : iris
    
"""

import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.0 사용안함
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split


# x, y data
iris = load_iris() 
x_data = iris.data
y_data = iris.target
y_data = y_data.reshape(-1,1)

obj = OneHotEncoder()
# sparse -> numpy
y_data = obj.fit_transform(y_data).toarray()
y_data.shape

x_train , x_test , y_train , y_test = train_test_split( x_data , y_data)

# x, y 변수 정의
X = tf.placeholder(dtype = tf.float32 , shape =[None , 4])
Y = tf.placeholder(dtype = tf.float32 , shape =[None , 3])

# =============================================================================
# Dnn network
# =============================================================================

hidden_node1 = 12
hidden_node2 = 6

# hidden layer1
w1 = tf.Variable(tf.random_normal([ 4 , hidden_node1]))
b1 = tf.Variable(tf.random_normal([ hidden_node1 ]))

# hidden layer2
w2 = tf.Variable(tf.random_normal([ hidden_node1 , hidden_node2]))
b2 = tf.Variable(tf.random_normal([ hidden_node2 ]))

# output layer 
w3 = tf.Variable(tf.random_normal([ hidden_node2 , 3]))
b3 = tf.Variable(tf.random_normal([ 3 ]))

# softmax 분류기 
# 1) 회귀방정식 : 예측치 
hidden_output1 = tf.nn.relu(tf.matmul(X, w1) + b1) # hidden layer 
hidden_output2 = tf.nn.relu(tf.matmul(hidden_output1, w2) + b2)
model = tf.matmul(hidden_output2 , w3) + b3                           
softmax = tf.nn.softmax(model) 

# 2) Loss
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(
    labels = Y , logits = model
    ))

# 3) optimizer : 오차 최소화(w, b update) 
train = tf.train.AdamOptimizer(0.1).minimize(loss) # 오차 최소화

# 4) argmax() : encoding -> decoding
y_pred = tf.argmax(softmax , axis =1)
y_true = tf.argmax(Y , axis =1)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    feed_data= { X : x_data , Y : y_data}
    
    #반복 학습
    for step in range(500):
        _, loss_val = sess.run([train , loss] , feed_dict = feed_data)
        
        if (step+1)% 50 == 0 :
            print(" step : {} , loss : {}".format(step+1 , loss_val))

    # model result
    y_pred_re = sess.run( y_pred , feed_dict ={ X :x_data })
    y_true_re = sess.run(y_true , feed_dict = { Y : y_data })
    
    print("y pred = " , y_pred_re)
    print("y true = " , y_true_re)
    acc = accuracy_score(y_true_re,y_pred_re)
    print("acc = " , acc)




















































