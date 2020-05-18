# -*- coding: utf-8 -*-
"""


"""

from knn_data import data_set
import numpy as np
# dataset 생성
know , not_know , cate = data_set()
know.shape
not_know
cate 

# 거리 계산식 : 차 > 제곱 > 합 > 제곱근
distance = np.sqrt(((not_know - know)**2 ).sum(axis=1))
distance

sortDist = distance.argsort()

result = cate[sortDist]
# array(['B', 'B', 'A', 'A'], dtype='<U1')

#최근접 3개 category
k3 = result[:3]

classfy_re = {}
for i in k3:
    classfy_re[i] = classfy_re.get(i,0) + 1
    
classfy_re
vote_re = max(classfy_re)
vote_re


def knn_classify( know , not_know , cate , k = 3):
    # 거리 계산식
    distance = np.sqrt(((not_know - know)**2 ).sum(axis=1))
    
    # 오름차순 정렬 -> index
    sortDist = distance.argsort()

    class_result ={}
    
    for i in range(k) : 
        key = cate[sortDist[i]]
        class_result[key] = class_result.get(key ,  0 ) + 1

    return max(class_result)

result = knn_classify(know , not_know , cate)
result









