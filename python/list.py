'''
list 특징

'''

# 1. 단일 list
lst = [1,2,3,4,5]
print(lst,type(lst))

for i in range(0,len(lst)):
    print(lst[i:])

for i in range(0,len(lst)):
    print(lst[:i])

print(lst[::2])

# 2. 중첩 list : [[],[],[]]
a= ['a','b','c']
b= [10,20,5,a,True,"hong"]
print(b)
print(b[3][1:])

print(id(a),id(b))

# 값 수정
num = ['one', 'two', 'three','four','six']
print(len(num))

num.append('five') # 원소 추가
num.insert(0,'zero') # 원소 추가
num.remove('five') # 원소 삭제
num[5] = 'end'
print(num)

# list 연산

# 1) list 결합
x = [1,2,3,4]
y= [1.5,2.5]
z = x+y
z = sorted(z)
print(z)
'''
# 2) list 확장
x.extend(y)
print(x)

# 3) list 추가
x.append(y)
print(x)
'''
# 4) list 곱셈
print(lst*4)
print("-"*100)
print(x)
# 5) sort 정렬
x.sort(reverse=True)
print(x)




dataset = []
size = int(input())
for i in range(size):
    dataset.append(i+1)

print(dataset)

# 7. list 에서 원소 찾기
'''
if value in list:
    참 실행문
else:
    거짓 실행문
'''

if 5 in dataset:
    print("yes")
else:
    print("no")