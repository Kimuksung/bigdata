
"""

    - softmax + iris

"""

import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.0 사용안함
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder

# x, y data
iris = load_iris() 
x_data = iris.data
y_data = iris.target
y_data = y_data.reshape(-1,1)

'''

encoder
0 -> 1 0 0
1 -> 0 1 0
2 -> 0 0 1

'''

obj = OneHotEncoder()
# sparse -> numpy
y_data = obj.fit_transform(y_data).toarray()
y_data.shape

# x, y 변수 정의
X = tf.placeholder(dtype = tf.float32 , shape =[None , 4])
Y = tf.placeholder(dtype = tf.float32 , shape =[None , 3])

# w , bias 
w= tf.Variable(tf.random_normal([4,3]))
b = tf.Variable(tf.random_normal([3]))

# softmax 분류기 
# 1) 회귀방정식 : 예측치 
model = tf.matmul(X, w) + b # 회귀모델 

# softmax(예측치)
softmax = tf.nn.softmax(model) 

# (2) loss function : Entropy 이용 : -sum(Y * log(model)) 

#1차 방법
#loss = -tf.reduce_mean(Y * tf.log(softmax) + (1 - Y) * tf.log(1 - softmax))

#2차 방법 : softmax  + crossentrophy
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

    import matplotlib.pyplot as plt
    plt.plot(y_pred_re ,color = 'r')
    plt.plot(y_true_re , color = 'b')



















