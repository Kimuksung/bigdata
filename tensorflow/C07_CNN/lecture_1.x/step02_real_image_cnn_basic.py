'''

'''
import tensorflow.compat.v1 as tf # ver1.x
tf.disable_v2_behavior() # ver2.0 사용안함

from matplotlib.image import imread #
import numpy as np
from tensorflow.keras.datasets.mnist import load_data # dataset load
import matplotlib.pyplot as plt

# 1. image read 
img = imread("C:/ITWILL/6_Tensorflow/workspace/C07_CNN/images/parrots.png")
plt.imshow(img)

img.shape # (512, 768, 3)

# 2. 실수형 변환 : int -> float32

# input image reshape  
inputImg = img.reshape(1,512,768,3) #(size , h , w, color)

# Filter 변수 정의 
Filter = tf.Variable(tf.random_normal([9,9,3,8])) # 난수 (row , column , color ,fmap) 
 
# 1. Convolution layer : 특징 추출
conv2d = tf.nn.conv2d( inputImg, Filter , strides=[1,2,2,1] , padding='SAME' )
print(conv2d) 

# 2. Pool layer : down sampling
pool = tf.nn.max_pool(conv2d, ksize=[1,7,7,1],strides=[1,4,4,1],padding = 'SAME')
print(pool) 


with tf.Session() as sess :
    sess.run(tf.global_variables_initializer()) # filter 초기화 
    
    # 합성곱 연산 
    conv2d_img = sess.run(conv2d)    
    conv2d_img = np.swapaxes(conv2d_img, 0, 3) # 축 교환 
    print("this:" , conv2d_img.shape) # (5, 28, 28, 1)
    
    for i, img in enumerate(conv2d_img) :
        plt.subplot(1, 8, i+1) # 1행5열,1~5 
        plt.imshow(img.reshape(256,384), cmap='gray') # 
    plt.show()
    
    # 폴링 연산 
    pool_img = sess.run(pool)
    pool_img = np.swapaxes(pool_img, 0, 3)
    
    for i, img in enumerate(pool_img) :
        plt.subplot(1,8, i+1) # 1행5열,1~5 
        plt.imshow(img.reshape(64,96), cmap='gray') 
    plt.show()



































