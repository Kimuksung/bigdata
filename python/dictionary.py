'''
dictionary 특징
- set 구조와 유사함
- key 와 value 한쌍으로 원소 구성
- key => value 참조
- key 중복 불가 , value 중복 가능
형식) 변수 ={key:value , key:value}

'''

# 1. dict 생성
# 방법1)
dic = dict(key1 = 100 , key2 = 200,key3 = 300)
print(dic,len(dic),type(dic))

# 방법2)
dic2 ={'name':'홍길동','age':35,'addr':"seoul"}
print(dic2,len(dic2),type(dic2))

# 2. 수정 추가 삭제 검색 : key 이용

dic2['age'] = 40
dic2['sal'] = 500
print(dic2,len(dic2),type(dic2))
del dic2['addr']
print(dic2,len(dic2),type(dic2))

# key 검색
print('age' in dic2)

# 3. for 이용
for i in dic2:
    print(i, dic2[i])
for j in dic2.values():
    print(j)

for k,v in dic2.items():
    print(k,v)

# 4. key -> value
print(dic2['name'])
print(dic2.get('name'))

# 5. one key multiple value
emp = dict(uksung=[550,50],namjun=[500,60],jung=[490,100])
print(emp)

for k,v in emp.items():
    if v[0]>=500:
        print(k+":"+str(v[0]+v[1]))

# 6. 문자 빈도수 구하기
charset = ['love','test','love','hello','test','love']
print(len(charset))
wc ={}

for word in charset:
    if word in wc:
        wc[word] += 1
    else:
        wc[word]=1

print(max(wc,key=wc.get))
