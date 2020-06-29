# -*- coding: utf-8 -*-
"""

1. text -> feature
    - 지도 학습에서 text 대상 sparse matrix
    - ex) tf , tfidf

2. num_words(max featrues)
    - 단어의 차수를 지정하는 속성
    ex) num_words : 500 / 전체 단어 1000에서 중요단어 500 선정

3. max length : padding 적용
    - 한 문장을 구성하는 단어 수 지정
    ex) max_length = 100 / 전체 문장을 구성하는 단어수 100개로 지정
    1문장 : 150개 구성 -> 50 짤림
    2문장 : 70개 단어 구성 -> 30개 0으로 채움
    
"""

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences # padding

# 토큰 생성기
tokenizer = Tokenizer(num_words = 6) # num_words 생략 : 전체 단어 이용
texts = ['The dog sat on the table.', 'The dog is my Poodle.']

# 1. create token
tokenizer.fit_on_texts(texts)
token = tokenizer.word_index # token 반환
print(token)

# 2. texts -> feature 추출
binary = tokenizer.texts_to_matrix(texts , mode ='binary')
binary # [docs , terms + 1]
# =============================================================================
# array([[0., 1., 1., 1., 1., 1., 0., 0., 0.],
#        [0., 1., 1., 0., 0., 0., 1., 1., 1.]])
# =============================================================================

count = tokenizer.texts_to_matrix(texts , mode ='count')
count
# =============================================================================
# array([[0., 2., 1., 1., 1., 1., 0., 0., 0.],
#        [0., 1., 1., 0., 0., 0., 1., 1., 1.]])
# =============================================================================

freq = tokenizer.texts_to_matrix(texts , mode ='freq')
freq
# =============================================================================
# array([[0.        , 0.33333333, 0.16666667, 0.16666667, 0.16666667,        0.16666667, 0.        , 0.        , 0.        ],
#        [0.        , 0.2       , 0.2       , 0.        , 0.        ,        0.        , 0.2       , 0.2       , 0.2       ]])
# 
# =============================================================================

tfidf = tokenizer.texts_to_matrix(texts , mode ='tfidf')
tfidf
# =============================================================================
# array([[0.        , 0.86490296, 0.51082562, 0.69314718, 0.69314718, 0.69314718, 0.        , 0.        , 0.        ],
#        [0.        , 0.51082562, 0.51082562, 0.        , 0.        , 0.        , 0.69314718, 0.69314718, 0.69314718]])
# 
# =============================================================================

tfidf.shape


# 3. max length : padding 적용
seq_index = tokenizer.texts_to_sequences(texts)
seq_index # [[1, 2, 3, 4, 1, 5], [1, 2]]

max_length = max([len(seq) for seq in seq_index])
max_length

x_data = pad_sequences(seq_index , maxlen = max_length)
x_data
# =============================================================================
# array([[1, 2, 3, 4, 1, 5],
#        [0, 0, 0, 0, 1, 2]])
# =============================================================================
x_data2 = pad_sequences(seq_index , maxlen = 4)
x_data2
# =============================================================================
# array([[3, 4, 1, 5],
#        [0, 0, 1, 2]])
# =============================================================================

