# -*- coding: utf-8 -*-
"""
1. 명사 추출 (Kkma)
2. 전처리 : 단어 길이 , 숫자 제외
3. 단어의 빈도수 출력
"""

import konlpy
from konlpy.tag import Kkma
from wordcloud import WordCloud

help(WordCloud)

kkma = Kkma()

file = open("../data/text_data.txt" , mode = 'r' , encoding = 'utf-8')
docs = file.read()
docs

# docs -> sentence
ex_sent = kkma.sentences(docs)
ex_sent

# docs -> nouns
ex_nouns = kkma.nouns(docs) # set 처리가 됨
ex_nouns

# 따라서 하나의 문장 마다 단어를 추출해야 단어의 갯수를 셀 수 있다.

nouns_word = [] # 명사 저장

for sentence in ex_sent :
    for noun in kkma.nouns(sentence):
        nouns_word.append(noun)

# data 전처리 + word count 
from re import match

nouns_count = {}

for i in nouns_word:
    if len(i) > 1 and not match('^[0-9]' , i):
        nouns_count[i] = nouns_count.get(i,0) +1

# World Cloud
# 1) top5 word
from collections import Counter 

word_count = Counter(nouns_count) # dict
top5 = word_count.most_common(5)

# Virtualization
wc = WordCloud(font_path = 'C:\\Windows\\Fonts\\malgun.ttf' , 
          width = 400 , height = 200 , max_words = 100 ,
          max_font_size = 150 , background_color = 'white'
          )

wc_result = wc.generate_from_frequencies(dict(top5) )
import matplotlib.pyplot as plt
plt.axis('off')
plt.imshow(wc_result)









