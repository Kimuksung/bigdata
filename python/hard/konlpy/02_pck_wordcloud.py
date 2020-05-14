# -*- coding: utf-8 -*-
"""

"""

import konlpy
from konlpy.tag import Kkma
from wordcloud import WordCloud

kkma = Kkma()

import pickle
file = open("../data/news_data.pck" , mode = 'rb')
month_news2 = pickle.load(file)
month_news2
len(month_news2)


word = []
for i in month_news2 :
    noun = kkma.nouns(i)
    for j in noun:
        word.append(j)

word_count ={}
from re import match

for i in word:
    if len(i) > 1 and not match('^[0-9]' , i):
        word_count[i] = word_count.get(i,0) +1

word_count
len(word)
len(word_count)

from collections import Counter 
word_cnt = Counter(word_count) # dict
word_cnt['확진자'] = word_cnt['진자']

del word_cnt['진자']

top100 = word_cnt.most_common(100)

wc = WordCloud(font_path = 'C:\\Windows\\Fonts\\malgun.ttf' , 
          width = 800 , height = 600 , max_words = 100 ,
          max_font_size = 150 , background_color = 'white'
          )

wc_result = wc.generate_from_frequencies(dict(top100) )
import matplotlib.pyplot as plt
plt.axis('off')
plt.imshow(wc_result)
























