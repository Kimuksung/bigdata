"""

multi linear regression : matrix multiply
    - X(n) -> Y
    - y_pred = X1 * a1 + X2 * a2 + ...
    - y_pred - tf.matmul(X , a ) + b
    
"""

import tensorflow as tf

# X , Y define
X = [[1.0 , 2.0]] # 1 x 2
Y = 2.5 

# a , b 변수 define : 수정 가능
a = tf.Variable(tf.random.normal([2,1])) # 기울기 2 x 1
b = tf.Variable(tf.random.normal([1]))

# model 식 정의
y_pred = tf.matmul(X , a) + b
print(y_pred.numpy())

#model error 
err = Y - y_pred

# loss function
loss = tf.reduce_mean(tf.square(err))

print("a = {} , b={}".format(a.numpy(), b.numpy()))
print("predict : {}".format(y_pred))
print("model error : {}".format(err))
print("loss function : {}".format(loss))


























