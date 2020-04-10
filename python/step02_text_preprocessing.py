# 텍스트 전처리
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']
print(len(texts), type(texts)) # 3 <class 'list'>

from re import sub # gsub() 유사함
# from package.module import class or function
# from module import class or function

# 1. 소문자 변경
print('소문자 변경')
texts_re = [ text.lower() for text in texts]
print('texts_re1 :', texts_re)

# 2. 숫자 제거
texts_re2 = [ sub('[0-9]', '', text) for text in texts_re]
print('texts_re2 :', texts_re2)

# 3. 문장부호 제거
punc_str = '[.,;:?!]'
texts_re3 = [sub(punc_str, '', text) for text in texts_re2]
print('texts_re3 :', texts_re3)

# 4. 특수문자 제거
spec_str = '[@#$%^&*()]'
texts_re4 = [sub(spec_str, '', text) for text in texts_re3]
print('texts_re4 :', texts_re4)

# 5. 공백 제거 : 'abtta a' -> ''.join('abtta', 'a') -> 'abttaa'
texts_re5 = [''.join(text.split()) for text in texts_re4]
print('texts_re5 :', texts_re5)
# texts_re5 : ['afabasabag', 'abttaa', 'uysfsfaa']