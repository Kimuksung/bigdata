'''

1. tfidf 가중치 기법 - sparse matrix
2. ham(0) / spam(1) -> discrete Y -> sigmoid
3. Hyperparameter
    - max features = 4000( input node )
    - batch_size = 500
    - iter isze = 10
    - lr = 0.01
    - epochs = 50
    1epochs = 500 * 10 => 5000
    
'''

import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.x 사용 안함 
from sklearn.preprocessing import OneHotEncoder # y data 
from sklearn.metrics import accuracy_score # model 평가
import matplotlib.pyplot as plt 
import numpy as np

x_train , x_test , y_train , y_test = np.load("C:/ITWILL/6_Tensorflow/data/spam_data.npy" ,allow_pickle = True)
x_train.shape # (3901, 4000)


y_train = np.array(y_train)
y_test = np.array(y_test)

y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)
y_test.shape

max_features = 4000 
batch_size = 500
iter_size = 10
lr = 0.01
epochs = 50
# X , Y 변수 정의
X = tf.placeholder( dtype = tf.float32 , shape= [None , max_features ])
y = tf.placeholder( dtype = tf.float32 , shape= [None , 1 ]) # ham / spam


hidden_node1 = 6
hidden_node2 = 3

# hidden layer1
w1 = tf.Variable(tf.random_normal([ max_features , hidden_node1]))
b1 = tf.Variable(tf.random_normal([ hidden_node1 ]))

# hidden layer2
w2 = tf.Variable(tf.random_normal([ hidden_node1 , hidden_node2]))
b2 = tf.Variable(tf.random_normal([ hidden_node2 ]))

# output layer 
w3 = tf.Variable(tf.random_normal([ hidden_node2 , 1]))
b3 = tf.Variable(tf.random_normal([ 1 ]))

#sigmoid classifier
hidden_output1 = tf.nn.relu(tf.matmul(X, w1) + b1) # hidden layer 
hidden_output2 = tf.nn.relu(tf.matmul(hidden_output1, w2) + b2)
model = tf.matmul(hidden_output2 , w3) + b3                           
sigmoid = tf.nn.sigmoid(model) 

#loss
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(
    labels = y , logits = model
    ))

# 3) optimizer : 오차 최소화(w, b update) 
train = tf.train.AdamOptimizer(lr).minimize(loss) # 오차 최소화

# 4) cut off
y_pred = tf.cast(sigmoid > 0.5 , tf.float32)

with tf.Session() as sess :
    sess.run(tf.global_variables_initializer()) # w, b 초기화  
    for epoch in range(epochs) : 
        tot_loss = 0
        for step in range(iter_size):
            idx = np.random.choice( a = x_train.shape[0] ,size = batch_size , replace =False)
            feed_data = { X : x_train[idx], y : y_train[idx]}
            _, loss_val = sess.run([train , loss] , feed_dict = feed_data)
            
            tot_loss += loss_val
        #1epoch 종료
        avg_loss = tot_loss / iter_size
        print("epoch = {} , loss = {}".format(epoch, avg_loss))
        
    # model test 
    feed_data2 = {X : x_test, y : y_test}
    y_pred_re = sess.run(y_pred, feed_dict = feed_data2)
    y_true_re = sess.run(y, feed_dict = feed_data2)
    
    acc = accuracy_score(y_true_re, y_pred_re)
    print("accuracy =", acc)




















