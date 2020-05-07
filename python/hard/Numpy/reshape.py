# -*- coding: utf-8 -*-
"""
1. image shape : 3d 
2. reshape

"""

import numpy as np
from matplotlib.image import imread # 이미지 읽기
import matplotlib.pylab as plt


# 1. image shape
file_path = 'C:\\ITWILL\\4_Python-II\\workspace\\chap04_Numpy\\images/test1.jpg'
image = imread(file_path)
type(image)
image

image.shape #(360, 540, 3)

plt.imshow(image)

# RGB 색상 분류
r = image[:,:,0] #r
g = image[:,:,0] #g
b = image[:,:,0] #b

r
r.shape

# 2. image data reshape

from sklearn.datasets import load_digits 

digit = load_digits()
digit.DESCR

x = digit.data # x변수
y = digit.target # y변수
x
x.shape #(1797, 64)

y
y.shape #(1797,)

x[0]
img_0 = x[0].reshape(8,8)

plt.imshow(img_0)

y[0]

X_3d = x.reshape(-1,8,8) # -1은 전부를 하겠다.
X_3d
X_3d.shape # (1797, 8, 8)


X_4d = X_3d[:,:,:,np.newaxis]
X_4d
X_4d.shape # (1797, 8, 8, 1)


# Normal Data Reshape
'''
전치 행렬 : T
swapaxis = 전치 행렬
transpose() : 3차원 이상 모양 변경
'''

# 1. 전치 행렬
data = np.arange(10).reshape(2,5)

data

type(data)

data.T

# 2. transpose()

'''
1d : 효과 x
2d : 전치행렬
3d : (면,행,열) -> (열,행,면)

'''

arr3d = np.arange(1,25).reshape(4,2,3)
arr3d
arr3d.shape #(4, 2, 3)


arr3d_transpose = arr3d.transpose(2,1,0) # (4, 2, 3) -> (3, 2, 4)
arr3d_transpose
arr3d_transpose.shape # (3, 2, 4)


# (4, 2, 3) -> (2, 3, 4)
arr3d_transpose = arr3d.transpose(1,2,0)
arr3d_transpose
arr3d_transpose.shape # (2, 3, 4)























