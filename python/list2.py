'''
리스트 내포
list에서 for문 사용
형식1) 변수 = [실행문 for 변수 in 열거형]
형식2) 변수 = [실행문 for 변수 in 열거형 객체 if 조건식]

'''

# 형식1)

# X각 변량에 제곱

x= [ 2,4,1,3,7]

data2 = [i**2 for i in x]

#data3 = [i for i in x if  x % 3==0]

# 내장함수 +리스트 내포
print(sum(x))
data4 =  [[1,3,5],[4,5],[7,8,9]]

result = [sum(d) for d in data4]
print(result)