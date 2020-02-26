# chapt 01 basic

# package + session
# how to use package
# function + workspace
# format : 'utf-8'

# 여러 줄 주석: ctrl + shift + c

# 1. pacakge
dim(available.packages()) #dim - 차원을 알려준다.행열

# 2. session
sessionInfo() # show session info
# R environment , OS , language info(local) ..

# 3. use package
# 1) install package
install.packages('stringr') #package dependencies
# 2) package 설치 경로
.libPaths()
# 3) in memory : 패키지 메모리에 업로드
library(stringr)

str_extract('홍길동35이순신45','[가-힣]{3}')

str_extract_all('홍길동35이순신45','[가-힣]{3}')
# 4) delete package
remove.packages('stringr') #dependencies들은 남아 있다.

# package error
# 1) Rstudio admin access
# 2) reinstall error -> remove.packages('패키지') -> os reboot -> install.packages('패키지')

# 4. data type
var1 <- 0 # var1=0
var1 <- 1
var2 <-10
var3 <-30
var1; var2;var3;

var3<- c(10,20,30,40,50)
var3

print(var1==var2)

#object
member.id='kimuksung'
member.name='김욱성'
member.age = 27

#scala(0차원) vs vector(1차원)
score <- 95 #scala
scores <- c(55,25,65,75) #vector

#숫자형,문자형,논리형
int<- 100
float<- 125.23
string<-"korea"
bool <- T
#자료형 확인
mode(int)
mode(float)#"numeric"
mode(bool)#"logical"
mode(string) #"character"
# is.xxxx
is.numeric(int)
is.character(string)
is.logical(bool)

datas <- c(1,2,3,NA,45)
mode(datas)
is.na(datas)
datas2 <- c(1,2,3,NA,4,'k')
mode(datas2)


#자료형 변환 - as
#(1) 문자형 -> 숫자형 변환
x<-c(10,20,30,'40') #vector
x*2 #error
x<-as.numeric(x)
x*2
x**2

plot(x)
plot(x**2)

#(2) 요인형(factor)
# 범주형 변수 생성

gender <- c('남','여','남','여','여')
mode(gender)

# 문자형 -> 요인형
fgender <- as.factor(gender)
plot(fgender)
fgender
str(fgender) #더미 변수 : 숫자에 의미가 없는 숫자형

#mode  vs class
mode(fgender) #자료형 확인
class(fgender) #자료구조 확인

x<-c(4,2,4,2)
mode(x) #numeric

f<-as.factor(x)
f
#요인형-> 숫자형 (level로 숫자로 반환하게 된다.)
x2<-as.numeric(f)
x2

#solution : 요인형-> 문자형 -> 숫자형 순으로 하여야 정상적인 값들을 recovery할 수 있다.

#---------------------------

# function 
# basic function : 바로 사용 가능하다. memory에 별도로 올리지 않아도 된다.
sessionInfo()

#패키지 도움말
library(help='stats')

#함수 도움말
help(sum)
x<- c(10,20,30,NA)
sum(x,na.rm=T)

?mean
mean(x,na.rm = T)


# 기본 데이터 셋
data()
data("Nile") # in memory
data(Nile)
mode(Nile)
plot(Nile)
hist(Nile)

# 작업 공간
getwd()
setwd("C:/ITWILL/2_Rwork/part-i")
getwd()

emp = read.csv("emp.csv",header = T)
emp
