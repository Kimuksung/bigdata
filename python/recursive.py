'''
rescursive function
- 자신의 function을 반복적으로 호출
- 반복적으로 변수의 값을 조정해서 연산 수행
ex) 1~n
- 반드시 종료 조건을 필요로 한다
'''

# 1. counter
stack =[]
def Counter(n):
    if n == 0 :
        print(0)
        return 0
    else:
        print(n)
        stack.append(n)
        Counter(n-1)
        #print(n)

Counter(3)
print(stack)
print(sum(stack))

# 2. 누적
def Adder(n):
    if n==1:
        return 1
    else:
        result = n + Adder(n-1)
    return result

print(Adder(1))