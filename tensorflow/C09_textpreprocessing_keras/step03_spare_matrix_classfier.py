# -*- coding: utf-8 -*-
"""

Sparse Matrix(Tfidf) + DNN model

1. csv file read
2. label +texts
3. tests 전처리 : 텍스트 벡터화
4. 희소행렬 
5. DNN model 생성 

"""

import pandas as pd
import numpy as np
import string
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model
from sklearn.metrics import accuracy_score

path = "C:/ITWILL/6_Tensorflow/data/temp_spam_data2.csv"

temp_spam = pd.read_csv(path , header= None , encoding = "utf-8")
temp_spam.info()

label = temp_spam[0]
texts= temp_spam[1]
label

# target dummy('spam'=1, 'ham'=0)
target = [1 if x=='spam' else 0 for x in label]
#print('target :', target)
target = np.array(target)

# data preprocessing
# texts 전처리
def text_prepro(texts):
    # Lower case
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts

texts = text_prepro(texts)

# 3. text의 토큰화
tokenizer = Tokenizer( num_words = 4000 ) # 약 8000개 중 4000개 단어
tokenizer.fit_on_texts(texts)
token = tokenizer.word_index
print("all words :" , len(token))

# 4. 희소 행렬(sparse matrix) : tfidf
x_data = tokenizer.texts_to_matrix(texts , mode ='tfidf')
x_data.shape # (5574, 4000)


# 5. split
x_train , x_val , y_train , y_val = train_test_split(x_data , target , test_size = 0.3)

# 6. DNN layer
input_shape = (4000,)

model = Sequential()
model.add(Dense(64 , input_shape = input_shape , activation = "relu"))
model.add(Dense(32 , activation = "relu"))
model.add(Dense(1 , activation = "sigmoid"))
model.summary()

# 7. model compile
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
model.fit(x_train , y_train , epochs = 5 ,validation_data = (x_val , y_val) , batch_size = 512)
loss , score = model.evaluate(x_val , y_val)
print("loss : ", loss)
print("accuracy : ", score)