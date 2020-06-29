# -*- coding: utf-8 -*-
"""

    1. 텍스트 벡터화
    - 텍스트를 숫자형 벡터로 변환
    - 작업 절차
    단계1 ) 텍스트 -> 토큰화(단어 / 문자)
    단계2 ) 정수 인덱스 : 토큰에 고유숫자 할당
    단계3 ) 인코딩 : 정수 인덱스 -> 숫자형 벡터 할당

    2. 인코딩 방법 : one-hot(sparse matrix) / word embedding
    
"""

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences # padding
from tensorflow.keras.utils import to_categorical # one-hot encoding

# 토큰 생성기
tokenizer = Tokenizer() # num_words 생략 : 전체 단어 이용

texts = ['The dog sat on the table.', 'The dog is my Poodle.']

# 1. create token
tokenizer.fit_on_texts(texts)
token = tokenizer.word_index # token 반환
print(token)
# {'the': 1, 'dog': 2, 'sat': 3, 'on': 4, 'table': 5, 'is': 6, 'my': 7, 'poodle': 8}

# 2. 정수 인덱스 : 토큰 -> 정수 인덱스(단어 순서)
seq_index = tokenizer.texts_to_sequences(texts)
print(seq_index) # [[1, 2, 3, 4, 1, 5], [1, 2, 6, 7, 8]]

# 3. padding : 정수 인덱스의 길이를 맞춰준다.
padding = pad_sequences(seq_index)
print(padding)

# 4. 인코딩(one-hot encoding) 
one_hot = to_categorical(padding)
print(one_hot)
one_hot.shape # (2, 6, 9)


