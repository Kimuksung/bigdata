"""
TFiDF 단어 생성기 : TfidfVectorizer  
  1. 단어 생성기[word tokenizer] : 문장(sentences) -> 단어(word) 생성
  2. 단어 사전[word dictionary] : (word, 고유수치)
  3. 희소행렬[sparse matrix] : 단어 출현 비율에 의해서 가중치 적용[type-TF, TFiDF]
    1] TF : 가중치 설정 - 단어 출현 빈도수
    2] TFiDF : 가중치 설정 - 단어 출현 빈도수 x 문서 출현빈도수의 역수            
    - tf-idf(d,t) = tf(d,t) x idf(t) [d(document), t(term)]
    - tf(d,t) : term frequency - 특정 단어 빈도수 
    - idf(t) : inverse document frequency - 특정 단어가 들어 있는 문서 출현빈도수의 역수
       -> TFiDF = tf(d, t) x log( n/df(t) ) : 문서 출현빈도수의 역수(n/df(t))
"""

from sklearn.feature_extraction.text import TfidfVectorizer

sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
]

# 1. 단어 생성기
tfidf = TfidfVectorizer()
tfidf

# 2. 문장 -> 단어 생성
tfidf_fit = tfidf.fit(sentences)
tfidf_fit


# word dictionary ( word : unique number)
vocs = tfidf_fit.vocabulary_
vocs # dict
len(vocs)

# 3. Sparse Matrix
spare_mat = tfidf.fit_transform(sentences)
type(spare_mat) # scipy.sparse.csr.csr_matrix

spare_mat.shape
print(spare_mat)
''' 
   row , col         weight(tfidf)
  (0, 3)        0.2205828828763741
  (0, 16)       0.2205828828763741
  (0, 25)       0.2205828828763741
  (0, 17)       0.2205828828763741
  (0, 10)       0.2205828828763741
  (0, 1)        0.2205828828763741
  (0, 30)       0.2205828828763741
  (0, 23)       0.1677589680512606
  (0, 24)       0.4411657657527482
  (0, 9)        0.1677589680512606
  (0, 15)       0.2205828828763741
  (0, 2)        0.2205828828763741
  (0, 11)       0.2205828828763741
  (0, 5)        0.26055960805891015
  (0, 14)       0.4411657657527482
  (1, 8)        0.3464378827197198
  (1, 19)       0.3464378827197198
  (1, 6)        0.4555241832708016
  (1, 20)       0.3464378827197198
  (1, 21)       0.3464378827197198
  (1, 23)       0.3464378827197198
  (1, 9)        0.3464378827197198
  (1, 5)        0.2690399207469689
  (2, 28)       0.27054287522550385
  (2, 12)       0.27054287522550385
  (2, 18)       0.27054287522550385
  (2, 4)        0.27054287522550385
  (2, 0)        0.27054287522550385
  (2, 26)       0.27054287522550385
  (2, 7)        0.27054287522550385
  (2, 29)       0.27054287522550385
  (2, 27)       0.27054287522550385
  (2, 22)       0.27054287522550385
  (2, 13)       0.27054287522550385
  (2, 8)        0.2057548299742193
  (2, 19)       0.2057548299742193
  (2, 20)       0.2057548299742193
  (2, 21)       0.2057548299742193
  (2, 5)        0.15978698032384395
'''

sparse_mat_arr =spare_mat.toarray()
sparse_mat_arr.shape
sparse_mat_arr













