# -*- coding: utf-8 -*-
"""
1. csv file read
2. texts , target -> 전처리
3. max features
4. Sparematrix

"""

import pandas as pd

# 1. csv file read
spam_data = pd.read_csv( "../data/temp_spam_data.csv" , encoding = "utf-8" , header = None )
spam_data 

target = spam_data[0] 
texts = spam_data[1]

# target = 2 category variable
# ham -> spam ->
target = [1 if t =='spam' else 0 for t in target]
target

# @ texts preprocessing
import string # text 전처리 

def text_prepro(texts): # input -> string -> 음절 -> 문장
    # Lower case
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts

texts_re = text_prepro(texts)
texts_re


'''
# 3. max features

- 사용할 X변수의 갯수 (열의 차수)

'''

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_fit = TfidfVectorizer().fit(texts_re)
vocs = tfidf_fit.vocabulary_
vocs
max_features = len(vocs) #16 -> sparse matrix [ 5 X 16]

# if max_features = 10 -> sparse matrix [ 5 X 10]


# @ sparse matrix

sparse_mat = TfidfVectorizer().fit_transform(texts_re)
# <5x16 sparse matrix of type '<class 'numpy.float64'>' with 18 stored elements in Compressed Sparse Row format>

sparse_mat2 = TfidfVectorizer(max_features = 10).fit_transform(texts_re)
# <5x10 sparse matrix of type '<class 'numpy.float64'>'	with 12 stored elements in Compressed Sparse Row format>


# @ scipy -> numpy
sparse_mat_arr = sparse_mat.toarray()
sparse_mat_arr.shape # (5, 16)

vocs
















