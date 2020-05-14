# -*- coding: utf-8 -*-
"""
konlpy : Korean 형태소 analysis package
"""

from konlpy.tag import Kkma
kkma = Kkma() 
para = "나는 홍길동입니다. 나이는 23세 입니다. 대한민국 만세"

ex_sent = kkma.sentences(para) # 문단 -> 문장
print(ex_sent)

ex_nouns = kkma.nouns(para) # 문단 -> 명사
print(ex_nouns)

# 문단 -> 품사(형태소)
ex_pos = kkma.pos(para)
ex_pos
type(ex_pos)

# NNG 일반 명사 NNP고유 명사 NP 대명사
nouns = []

for word , wclass in ex_pos:
    if wclass == "NNG" or wclass =="NNP" or wclass =="NP":
        nouns.append(word)
        
nouns
