'''
1. pickle file laod
2. text 전처리
3. word count
'''

import pickle

# 1. pickle file load
file = open("../data/new_crawling.pickle" , mode= 'rb')
news_crawling = pickle.load(file)

print(type(news_crawling))
print(news_crawling)

# 2. 텍스트 전처리
def clean_text(texts) :
    from re import sub  # gsub() 유사함
    # 1. 소문자 변경
    texts_re = texts.lower() # 문장 1개 소문자 변경
    # 2. 숫자 제거
    #texts_re2 = sub('[0-9]', '', texts_re)
    # 3. 문장부호 제거
    punc_str = '[.,;:?!]'
    texts_re3 = sub(punc_str, '', texts_re)
    # 4. 특수문자 제거
    spec_str = '[@#$%^&*()]'
    texts_re4 = sub(spec_str, '', texts_re3)
    # 5. 공백 제거
    texts_re5 = ' '.join(texts_re4.split())

    return texts_re5

clean_news = [clean_text(i) for i in news_crawling]
print(clean_news)

word_count = {}
for texts in clean_news:
    for word in texts.split(" "):
        word_count[word] = word_count.get(word,0) + 1

print(word_count)
answer = sorted(word_count.items(),key=lambda x:x[1] , reverse=True)
print("-"*30)
print(answer)

word_count2 = word_count.copy()
# 2음절 이상의 단어만 선택
for word in word_count.keys():
    if len(word) <2 :
        del word_count2[word]

print(word_count2)

# top 10 keyword
'''
pip install collection-extended
'''


from collections import Counter
count = Counter(word_count2)

del count['[바로잡습니다]']

top5 = count.most_common(10)
print("top 5 : ", top5)

import pandas as pd
df = pd.DataFrame(top5,columns=['word','freq'])

print(df)

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 선 그래프
plt.plot(df.word , df.freq)
plt.title('top10 word count 선그래프')
plt.show()

# 막대 그래프
plt.bar(df.word , df.freq)
plt.title('top10 word count 막대 그래프')
plt.show()