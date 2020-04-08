'''
반복문
while 조건식:

'''

cnt = tot = 0
'''
while cnt<10 :
    #pass
    cnt +=1
    tot += cnt
    print(cnt ,tot)

data = []
while cnt <101:
    tot += cnt
    if cnt %2==0:
        data.append(cnt)
    cnt+=1

print(tot)
print(data)
'''
data = []
while cnt < 101:
    if cnt %5==0 and cnt %3 !=0:
        data.append(cnt)
    cnt +=1
print(data)
'''
while(True):
    num = int(input())
    if num==0:
        break

import random # 난수 생성
r = random.random() # 0~1 난수 생성
print(r)

temp =[]
while True:
    r = random.random()
    if r< 0.01:
        break
    temp.append(r)

print(len(temp))

r = random.randint(1,5)

import random
print(" 숫자 맞추기 게임 ")
r = random.randint(1, 9)
while(True):
    user = int(input())
    if r > user:
        print("big")
    elif r == user:
        print("answer")
        break
    else:
        print("small")

# continue break
for i in range(1,10):
    print(i)

# string 열거형 객체
string ="my name is kimuksung"
for i in string:
    print(i,end=' ')
print()
for i in string.split():
    print(i, end="/")

# list 열거형 객체
lst = [1,2,3,4,5]
lst2 = [
    [1,2],
    [3,4],
    [5,6],
    [9,10],
    [7,8]
]
print(type(lst))
print(type(lst2))
for i in lst2:
    print(i)

print(list(sorted(lst2,key=lambda l:l[1])))
print(list(map(lambda x:x*x,lst)))
print(list(map(lambda x:x*1.5,range(10))))

# 3. range 열거형 객체
num1 = range(1,10,2)
print(list(num1))

# 4. list + range
idx = range(5)
print(list(idx))
'''
# index 이용 : 분류 정확도
y= [1,0,2,1,0] #관측치 : 범주형(0,1,2)
y_pred = [1,0,2,0,0] # 예측치

fit=[]
for i in range(len(y)):
    fit.append(int(y[i] == y_pred[i]))

print(fit.count(1)/len(fit))

# 5. 이중 for문
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")

# 문자열 처리 문단->문장->단어

para = """my name is kimuksung
address seoul
age 35. 
"""

for i in para.split('\n'):
    for j in i.split():
        print(j)

# if 값 in 열거형 객체 : 해당 값이 있으면 True 없으면 False
if "hello" in "name":
    print("yes")
else:
    print("No")