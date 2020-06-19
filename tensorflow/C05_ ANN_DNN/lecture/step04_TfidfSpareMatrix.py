# -*- coding: utf-8 -*-
"""
1. csv file read
2. texts , target -> 전처리
3. max features
4. Sparematrix

"""

import pandas as pd

# 1. csv file read
spam_data = pd.read_csv( "C:/ITWILL/6_Tensorflow/data/temp_spam_data2.csv" , encoding = "utf-8" , header = None )
spam_data 

target = spam_data[0] 
texts = spam_data[1]

# target = 2 category variable
# ham -> spam ->
target = [1 if t =='spam' else 0 for t in target]
target

# @ texts preprocessing

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_fit = TfidfVectorizer().fit(texts)
vocs = tfidf_fit.vocabulary_
vocs # 8722
max_features = 4000 

# @ sparse matrix
sparse_mat = TfidfVectorizer(stop_words = 'english', max_features = max_features).fit_transform(texts)

# @ scipy -> numpy
sparse_mat_arr = sparse_mat.toarray()
sparse_mat_arr.shape  # (5574, 4000)
print(sparse_mat)
print(sparse_mat_arr)

vocs

# @ train / test split
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split( sparse_mat_arr , target , test_size = 0.3 )

x_train.shape
x_test.shape

spam_data_split = (x_train , x_test , y_train , y_test)

# numpy binary file save
import numpy as np
np.save("C:/ITWILL/6_Tensorflow/data/spam_data" , spam_data_split)

# numpy binary file load
x_train , x_test , y_train , y_test = np.load("C:/ITWILL/6_Tensorflow/data/spam_data.npy" ,allow_pickle = True)
x_train.shape









