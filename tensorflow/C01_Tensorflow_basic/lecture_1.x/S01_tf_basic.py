# -*- coding: utf-8 -*-

'''
python code vs tensorflow code
'''

# python : 직접 실행 환경

import tensorflow as tf # version 2.0
import tensorflow.compat.v1 as tf # tensorflow 1.x

tf.disable_v2_behavior() # version 2.x 사용 X

#프로그램 정의 영역
x = tf.constant(10)
y = tf.constant(20) # 상수 정의
print(x,y)

z = x+y
print(z)

# session 객체 생성
sess = tf.Session() #상수 변수 식 -> device(Cpu , Gpu , Tpu) 할당

# 프로그램 실행 영역
print("x=" , sess.run(x))
print("y=" , sess.run(y))

print("z=" , sess.run(z))

# sess.run(x,y)  -> error
x_val , y_val = sess.run([x,y])
print(x_val , y_val)

sess.close()













