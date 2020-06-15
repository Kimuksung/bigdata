'''
문) image.jpg 이미지 파일을 대상으로 파랑색 우산 부분만 slice 하시오.
'''

import matplotlib.image as mp_image
import tensorflow as tf

import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout)

filename = "C:/ITWILL/6_Tensorflow/data/image.jpg"
input_image = mp_image.imread(filename)
input_image.shape


import matplotlib.pyplot as plt 
plt.subplot(1,2,1)
plt.imshow(input_image)
plt.show() 

# x = 30 ~ 570 y = 110
plt.subplot(1,2,2)
img_slice = tf.slice(input_image, [110,20,0],[-1,550,-1])

plt.imshow(img_slice)
plt.show()

 
