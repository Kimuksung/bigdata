# -*- coding: utf-8 -*-
"""

SVD 알고리즘 적용 - 추천 시스템

"""

from surprise import SVD , accuracy  # model 생성 평가
from surprise import Reader , Dataset # dataset 생성
import pandas as pd

ratings = pd.read_csv('movie_rating.csv')
print(ratings)
#  평가자[critic]   영화[title]  평점[rating]

# 1. rating dataset 생성
reader = Reader(rating_scale = (1,5))

dataset = Dataset(reader).load_from_df(ratings[['critic','title','rating']] , reader)

train = dataset.build_full_trainset()
test = train.build_anti_testset()

svd = SVD()
model = svd.fit(train)
pred = model.test(test)
pred # 전체 사용자 대상 예측치

'''
uid : 사용자 / iid : 영화 / r_ui = 실제 평점 / est: 예측치 평점
[Prediction(uid='Jack', iid='Just My', r_ui=3.225806451612903, est=3.194074693471826, details={'was_impossible': False}),
 Prediction(uid='Claudia', iid='Lady', r_ui=3.225806451612903, est=3.2212521299141224, details={'was_impossible': False}),
 Prediction(uid='Toby', iid='Lady', r_ui=3.225806451612903, est=3.400193057168381, details={'was_impossible': False}),
 Prediction(uid='Toby', iid='The Night', r_ui=3.225806451612903, est=3.3519934962060316, details={'was_impossible': False}),
 Prediction(uid='Toby', iid='Just My', r_ui=3.225806451612903, est=2.9811028929676, details={'was_impossible': False})]
'''

# 4. 개별 사용자 대상 예측치
user_id = "Toby" # 추천 대상자
items_id = ['The Night' , 'Just My' , 'Lady']
actual_rating = 0 # 실제 평점

for item in items_id:
    print(model.predict( user_id , item , actual_rating))

'''
user: Toby       item: The Night  r_ui = 0.00   est = 3.35   {'was_impossible': False}
user: Toby       item: Just My    r_ui = 0.00   est = 2.98   {'was_impossible': False}
user: Toby       item: Lady       r_ui = 0.00   est = 3.40   {'was_impossible': False}
'''








