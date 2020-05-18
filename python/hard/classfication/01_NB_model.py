# -*- coding: utf-8 -*-
"""
NB model 
    - GaussianNB : x variable is continous , normalize
    - MultinomialNB : high demension data like Sparse Matrix classfication
"""


import pandas as pd #csv file read
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB , MultinomialNB # modeling
from sklearn.metrics import accuracy_score , confusion_matrix , f1_score  # model 평가 하기위해
from scipy import stats # normalize test

# GaussianNB
iris = pd.read_csv("iris.csv")
iris.info()

#normalize test
stats.shapiro(iris['Sepal.Width'])
# (0.9849170446395874, 0.10113201290369034) 
# p-value - 0.10113201290369034 > 0.05 that's normalize

cols = list(iris.columns)
x = cols[:-1]
y = cols[-1]

train , test = train_test_split(iris , test_size = 0.3 , random_state = 123 )
train.shape

#modeling
nb = GaussianNB()
model = nb.fit( train[x] , train[y])
model

# accurancy
y_pred = model.predict(test[x])
y_true = test[y]


acc = accuracy_score(y_true , y_pred) # 분류 정확도
con_mat = confusion_matrix(y_true , y_pred) # 교차 분할표
f1_score = f1_score(y_true , y_pred , average = 'micro') # 불균형인 경우


#############################

# MultiNomial NB


from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
newsgroups = fetch_20newsgroups(subset='all') # 'train', 'test'
# Downloading 20news dataset.

print(newsgroups.DESCR)

'''
X variable : news article 내용
Y variable : news group (20)
'''

newsgroups.target_names
'''
'alt.atheism',
 'comp.graphics',
 'comp.os.ms-windows.misc',
 'comp.sys.ibm.pc.hardware',
 '''
cats = newsgroups.target_names[:4]

# 1) text -> sparse matrix
news_train = fetch_20newsgroups(subset='train' , categories = cats)
news_train.data # X variable
news_train.target # Y variable

#sparse Matrix
tfidf = TfidfVectorizer()
sparse_matrix = tfidf.fit_transform(news_train.data)
sparse_matrix.shape


# 2) modeling
nb =  MultinomialNB()
model = nb.fit(sparse_matrix , news_train.target)


# 3) model 평가 : fetch_20newsgroups(subset='test') 
news_test = fetch_20newsgroups(subset='test' , categories = cats)

news_test.data #text
news_test.target

sparse_test = tfidf.transform(news_test.data)
sparse_test

y_pred = model.predict(sparse_test)
y_true = news_test.target

acc = accuracy_score(y_true , y_pred)
acc # 0.8520749665327979

con_mat = confusion_matrix(y_true , y_pred)
con_mat
'''
array([[312,   2,   1,   4],
       [ 12, 319,  22,  36],
       [ 16,  26, 277,  75],
       [  1,   8,  18, 365]], dtype=int64)
'''


y_pred[:20]
y_true[:20]











































