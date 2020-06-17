# -*- coding: utf-8 -*-
"""


"""

import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.0 사용안함

from sklearn.metrics import accuracy_score

# x, y data 
# x : [hours, video]
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]] # [6,2]

# y : binary data (fail or pass)
y_data = [[0], [0], [0], [1], [1], [1]]  # [6,1]

# x, y 변수 정의
X = tf.placeholder(dtype = tf.float32 , shape = [None , 2])
Y = tf.placeholder(dtype = tf.float32 , shape = [None , 1])

# w , b
w = tf.Variable(tf.random_normal([2,1]))
b = tf.Variable(tf.random_normal([1]))

# sigmoid classify
# (1) model : 예측치 
model = tf.matmul(X, w) + b 
sigmoid = tf.sigmoid(model)  

# (2) loss function : Entropy 수식 = -sum(Y * log(model)) 
loss = -tf.reduce_mean(Y * tf.log(sigmoid) + (1-Y) * tf.log(1-sigmoid))

# (3) optimizer 
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss) 

#(4) cut-off :0.5
cut_off = tf.cast(sigmoid > 0.5 , tf.float32)

# model training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    feed_data = { X : x_data , Y : y_data }
    
    for step in range(500):
        _, loss_val = sess.run([train , loss] , feed_dict = feed_data)
        
        if (step+1) %50 == 0 :
            print("step = {} , loss = {}".format(step+1 , loss_val))

    #model 최적화
    y_true = sess.run(Y , feed_dict = {Y : y_data})
    y_pred = sess.run(cut_off , feed_dict = { X : x_data})
    
    acc = accuracy_score(y_true , y_pred)
    print("acc :" , acc)


















