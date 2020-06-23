'''

자동 미분 계수
    - tf.GradientTape
    - back step 이용
    - 딥러닝 모델 핵심 최적화 기술
    - 가중치(w)에 대한 오차(loss)의 미분값 계산 
    -> w에 대한 loss의 기울기

'''

import tensorflow as tf

'''
한 점 A(2,3)을 지나는 접선의 기울기
2차 방정식 : y = x^2 + x
'''

x = tf.Variable(2.0)
with tf.GradientTape() as tape :
    y = tf.math.pow(x,2) + x

    grad = tape.gradient(y , x)
    print(grad.numpy())
    

# x = 2.0 -> 1.0

x = tf.Variable(1.0)
with tf.GradientTape() as tape :
    y = tf.math.pow(x,2) + x

    grad = tape.gradient(y , x)
    print(grad.numpy())

x = tf.Variable(-1.0)
with tf.GradientTape() as tape :
    y = tf.math.pow(x,2) + x

    grad = tape.gradient(y , x)
    print(grad.numpy())

x = tf.Variable(-0.5)
with tf.GradientTape() as tape :
    y = tf.math.pow(x,2) + x

    grad = tape.gradient(y , x)
    print(grad.numpy())

# 미분값 양수 -> w(감소) -> 최솟점 하강
# 미분값 음수 -> w(증가) -> 최솟점 하강
























