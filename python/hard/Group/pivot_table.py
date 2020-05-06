# -*- coding: utf-8 -*-
"""
Pivot table
    - 사용자가 행,열 그리고 교차셀에 변수를 지정하여 테이블 생성
"""

import pandas as pd

pivot_data = pd.read_csv("pivot_data.csv")

pivot_data.info()
'''
교차셀 : 매출액(price)
행 : 연도(year) , 분기(quarter)
열 : 매출 규모(size)
셀에 적용할 통계 : sum
'''

ptable = pd.pivot_table(pivot_data, values = 'price' , index =['year','quarter'],columns = 'size',aggfunc = 'sum')

ptable
ptable.shape

ptable.plot(kind='barh',title='2016 vs 2017')


movie_data = pd.read_csv("movie_rating.csv")
movie_data.info()

movie = pd.pivot_table(movie_data, index=['title'], columns='critic',values='rating' ,aggfunc='sum')
movie.plot(kind='barh' , title =  'movie')
