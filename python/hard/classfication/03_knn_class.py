# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:40:12 2020

@author: user
"""

from knn_data import data_set
know ,not_know , category = data_set()

class KNNClassfy :
    #생성자 멤버
    
    def knn_classify( self , know , not_know , cate , k = 3):
        # 거리 계산식
        import numpy as np
        distance = np.sqrt(((not_know - know)**2 ).sum(axis=1))
        
        # 오름차순 정렬 -> index
        sortDist = distance.argsort()
    
        self.class_result ={}
        
        for i in range(k) : 
            key = cate[sortDist[i]]
            self.class_result[key] = self.class_result.get(key ,  0 ) + 1
        
    def vote(self):
        vote_re = max(self.class_result)
        print("answer :" ,vote_re)    

knn = KNNClassfy()
knn.knn_classify(know,not_know, cate)
knn.vote()
