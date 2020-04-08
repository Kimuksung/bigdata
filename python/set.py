'''
set 특징
- 순서가 없다(index 사용 불가)
- 중복 허용 불가

형식) 변수 = {값1, 값2, 값3}
- 집합 개념
'''

s = {1,3,5,5}
print(len(s))

print(s)

s2 = {3,6}

#집합 관련 function
print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))

gender = ['남자','여자','남자','여자']
print(set(gender))
print(list(set(gender)))

s3 = { 1,3,5,7}
s3.add(9)
print(s3)

s3.discard(3)
print(s3)