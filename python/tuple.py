'''
tuple 특징
- 순서가 존재한다.
- 1차원의 배열 구조
- 수정 불가 , 처리 속도 빠르다.
- 제공 함수 없다.
변수 = (원소1,원소2,...)

'''

tp = 10 #scala
tp1 = (10,)

print(type(tp),type(tp1))

tp3 = (10,32,213,23,23)
print(tp3[-3:])
# tp3[0] = 100 수정을 할 수 없다.
for i in tp3:
    print(i)
print("---"*10)
print(max(tp3))

# list -> tuple
lst = list(range(10000))
lst = tuple(lst)
print(type(lst))
lst = list(lst)
print(type(lst))
