# <실습> 산술연산자 
num1 <- 100 # 피연산자1
num2 <- 20  # 피연산자2
result <- num1 + num2 # 덧셈
result # 120
result <- num1 - num2 # 뺄셈
result # 80
result <- num1 * num2 # 곱셈
result # 2000
result <- num1 / num2 # 나눗셈
result # 5

result <- num1 %% num2 # 나머지 계산
result # 0

result <- num1^2 # 제곱 계산(num1 ** 2)
result # 10000
result <- num1^num2 # 100의 20승
result # 1e+40 -> 1 * 10의 40승과 동일한 결과


# <실습> 관계연산자 
# (1) 동등비교 
boolean <- num1 == num2 # 두 변수의 값이 같은지 비교
boolean # FALSE
boolean <- num1 != num2 # 두 변수의 값이 다른지 비교
boolean # TRUE

# (2) 크기비교 
boolean <- num1 > num2 # num1값이 큰지 비교
boolean # TRUE
boolean <- num1 >= num2 # num1값이 크거나 같은지 비교 
boolean # TRUE
boolean <- num1 < num2 # num2 이 큰지 비교
boolean # FALSE
boolean <- num1 <= num2 # num2 이 크거나 같은지 비교
boolean # FALSE

# <실습> 논리연산자(and, or, not, xor)
logical <- num1 >= 50 & num2 <=10 # 두 관계식이 같은지 판단 
logical # FALSE
logical <- num1 >= 50 | num2 <=10 # 두 관계식 중 하나라도 같은지 판단
logical # TRUE

logical <- num1 >= 50 # 관계식 판단
logical # TRUE
logical <- !(num1 >= 50) # 괄호 안의 관계식 판단 결과에 대한 부정
logical # FALSE

x <- TRUE; y <- FALSE
xor(x,y) # [1] TRUE
x <- TRUE; y <- TRUE
xor(x,y) # FALSE

x=10
y=5
z= x*y
if(z>=20){
  cat('실행됩니다.')
}else{
  
}

num<-scan()
if(num[1]%%2==0){
  cat('짝수')
}else{
  cat('홀수')
}


# 주민 번호를 이용하여 성별 판별하기
library(stringr)
jumin = "940817-1025525"
str_sub(jumin,8,8)

score<-c(78,75,83,97,12,43)
grade<- ifelse(score>=60,"합격","실패")
grade


excel<-read.csv(file.choose())
excel
str(excel)

#5점 척도
q5<-excel$q5
table(q5)
length(q5)

q5_re<- ifelse(q5>=3,"큰값","작은값")
#5점 척도 -> 범주형 data(2개로 나누어진다.)
table(q5_re)

# NA-> 평균 대체
x<-c(75,82,42,NA,85)
x_na<-ifelse(is.na(x),mean(x,na.rm = T), x)
x_na
