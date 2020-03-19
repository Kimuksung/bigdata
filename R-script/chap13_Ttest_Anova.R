
##################################
##  표본의 확률분포
##################################
# 모집단으로 부터 추출한 표본들의 통계량에 대한 분포 
# - z, chi^2, t, f분포


# 1. z분포(표준정규분포) 
# 모집단의 모표준편차(σ)/모분산(σ^2)이 알려진 경우 사용 
# 용도: 평균치와 표준편차를 달리하는 모든 정규분포를 µ=0, σ=1을 
# 갖는 표준정규분포로 표준화 
# 표준화공식(Z) = (X - mu) / sigma : 정규분포 -> 표준정규분포 

# 2. chi^2 분포
# 표준정규분포를 따르는 변수의 제곱합에 대한 분포
# chi^2 =  (X - mu)^2 / sigma^2 : 표준정규분포 Z를 제곱한 것
# 몇개를 합햇는냐에 따라서 카이제곱분포의 모수인 '자유도'가 결정 
# 용도: 정규분포를 따르는 변수의 분산에 대한 신뢰구간을 구할 때 이용 

# 3. t분포
# 모집단의 모표준편차(σ)/모분산(σ^2)이 알려지지 않은 경우 사용
# z분포와 유사
# 용도: 정규분포를 따르는 집단의 평균에 대한 가설검정(모평균 추정)
#  or 두 집단의 평균차이 검정을 할 경우 이용
# 표본의 표준편차(S)를 이용하여 모집단 추정 
# T =  (X - mu) / S -> 표본의 표준편차 

# 4. F분포
# 두 카이제곱분포를 각각의 자유도로 나눈 다음, 그것의 비율을 나타낸 분포 
# 서로 다른 카이제곱 분포의 비율의 형태로 표현 
# F = V1/u1 / V2/u2
# 용도: 정규분포를 따르는 두 집단의 분산에 대한 가설검정을 할 경우 이용 


#########################
# 표준화  vs 정규화
#########################

# 1. 표준화 : 척도 일치

# 1. 표존화 : 척도(평균 0, 표준편차 = 1 ) 일치
# =>정규분포 => 표준정규 본부

n = 1000
z = rnorm(n,mean=100,sd=10)
shapiro.test(z)
hist(z, freq=F)

# 1) 표준화 공식
# (Z) = (X - mu) / sigma 
mu=mean(z)
z = (z-mu)/ sd(z)
mean(z)
sd(z)

# 2) 표준화 함수
z2 = scale(z)
mean(z2)
sd(z2)
hist(z, freq=T)

# 2. 정규화(normalization) : 값의 범위(0~1) 일치
# x1 = -100~100  , x2 = -0.1~0.9 , x3(-1000~1000)
# - 서로 다른 변수의 값을 일정한 값으로 조정
# nor = (x - min ) / (max - min)

nor = function(x){
  return((x - min(x) ) / (max(x) - min(x)))  
}

summary(iris[-5])

nor_re = apply(iris[-5],2,nor)

summary(nor_re)

#----------

#############################################
# 추론통계분석 - 1-1. 단일집단 비율차이 검정
#############################################
# - 단일 집단(new)의 비율이 어떤 특정한 값(old)과 같은지를 검증

# 1. 실습데이터 가져오기
data <- read.csv("one_sample.csv", header=TRUE)
head(data)
x <- data$survey
x

# 2. 빈도수와 비율 계산
summary(x) # 결측치 확인
length(x) # 150개
table(x) # 0:불만족(14), 1: 만족(136) 
prop.table(table(x))

install.packages("prettyR")
library(prettyR) # freq() 함수 사용
freq(x) 

# 3. 가설검정 
#귀무가설(H0) : 기존 2014년도 고객 불만율과 2015년도 CS교육 후 불만율에 차이가 없다
# 형식) binom.test(성공횟수, 시행횟수, p = 확률)

# 1) 불만족율 기준 검정
# 양측검정 : 귀무가설 채틱 / 기각 결정
binom.test(14, 150, p=0.2) # 기존 20% 불만족율 기준 검증 실시
binom.test(14, 150, p=0.2, alternative="two.sided", conf.level=0.95)
#number of successes = 14, number of trials = 150, p-value = 0.0006735
#p-value < 0.05 -> 귀무가설(H0) 기각 -> 차이가 있다. 


# 방향성이 있는 대립가설 검정 : new > old   X
binom.test(14, 150, p=0.2, alternative="greater", conf.level=0.95)

# [실습]방향성이 있는 대립가설 검정 : new < old  O
binom.test(14, 150, p=0.2, alternative="less", conf.level=0.95)
#number of successes = 14, number of trials = 150, p-value = 0.0003179
# p-value <0.05  효과가 있다.

#############################################
# 추론통계분석 - 1-2. 단일집단 평균차이 검정
#############################################
# - 단일 집단의 평균이 어떤 특정한 값과 차이가 있는지를 검증
# t분포 용도: 정규분포를 따르는 집단의 평균에 대한 가설검정

# 1. 실습파일 가져오기
data <- read.csv("one_sample.csv", header=TRUE)
str(data) # 150
head(data)
x <- data$time
head(x)

# 2. 기술통계량 평균 계산
summary(x) # NA-41개
mean(x) # NA
mean(x, na.rm=T) # NA 제외 평균(방법1)

x1 <- na.omit(x) # NA 제외 평균(방법2)
mean(x1)

# 3. 정규분포 검정
# 정규분포(바른 분포) : 평균에 대한 검정 
# 정규분포 검정 귀무가설 : 정규분포와 차이가 없다.
# shapiro.test() : 정규분포 검정 함수

shapiro.test(x1) # 정규분포 검정 함수(p-value = 0.7242) 
# p-value >= 0.05 -> t.test()
# p-value < 0.05 -> wilcox.test()

# 4. 가설검정 - 모수/비모수  
# 정규분포(모수검정) -> t.test()
# 비정규분포(비모수검정) -> wilcox.test()

# 1) 양측검정 - 정제 데이터와 5.2시간 비교
t.test(x1, mu=5.2) 
t.test(x1, mu=5.2, alter="two.side", conf.level=0.95) # p-value = 0.0001417
#  t = 3.9461, df = 108, p-value = 0.0001417
# t 검정 통계량 채택역: -1.96~ 1.96
# 해설 : 평균 사용시간 5.2시간과 차이가 있다.

# 2) 방향성이 있는 연구가설 검정: new >= old o
t.test(x1, mu=5.2, alter="greater", conf.level=0.95) 
# p-value = 7.083e-05 <0.05 채택

t.test(x1, mu=5.2, alter="less", conf.level=0.95) 
# p-value = 0.999999 > 0.05 기각

#############################################
# 추론통계분석 - 2-1. 두집단 비율차이 검정
#############################################

# 1. 실습데이터 가져오기
data <- read.csv("two_sample.csv", header=TRUE)
data
head(data) # 변수명 확인


# 2. 두 집단 subset 작성
data$method # 1, 2 -> 노이즈 없음
data$survey # 1(만족), 0(불만족)

# - 데이터 정체/전처리
x<- data$method # 교육방법(1, 2) -> 노이즈 없음
y<- data$survey # 만족도(1: 만족, 0:불만족)
x;y

# 1) 데이터 확인
# 교육방법 1과 2 모두 150명 참여
table(x) # 1 : 150, 2 : 150
# 교육방법 만족/불만족
table(y) # 0 : 55, 1 : 245

# 2) data 전처리 & 두 변수에 대한 교차분석
table(x, y, useNA="ifany") 


# 3. 두집단 비율차이검증 - prop.test()

# 양측가설 검정
prop.test(c(110,135), c(150, 150)) # 14와 20% 불만족율 기준 차이 검정
prop.test(c(110,135), c(150, 150), alternative="two.sided", conf.level=0.95)

# # 방향성이 있는 대립가설 검정  
prop.test(c(110,135), c(150, 150), alternative="greater", conf.level=0.95)

#############################################
# 추론통계분석 - 2-2. 두집단 평균차이 검정
#############################################

# 1. 실습파일 가져오기
data <- read.csv("two_sample.csv")
data 
head(data) #4개 변수 확인
summary(data) # score - NA's : 73개

# 2. 두 집단 subset 작성(데이터 정제,전처리)
#result <- subset(data, !is.na(score), c(method, score))
dataset <- data[c('method', 'score')]
table(dataset$method)


# 3. 데이터 분리
# 1) 교육방법 별로 분리
method1 <- subset(dataset, method==1)
method2 <- subset(dataset, method==2)

# 2) 교육방법에서 점수 추출
method1_score <- method1$score
method2_score <- method2$score

# 3) 기술통계량 
length(method1_score); # 150
length(method2_score); # 150

mean(method1_score,na.rm=T)
mean(method2_score,na.rm=T)

# 4. 분포모양 검정 : 두 집단의 분포모양 일치 여부 검정
var.test(method1_score, method2_score) 
# 동질성 분포 : t.test()
# 비동질성 분포 : wilcox.test()

# 5. 가설검정 - 두집단 평균 차이검정
t.test(method1_score, method2_score)
t.test(method1_score, method2_score, alter="two.sided", conf.int=TRUE, conf.level=0.95)
# p-value = 0.0411 - 두 집단간 평균에 차이가 있다.

# # 방향성이 있는 연구가설 검정 
t.test(method1_score, method2_score, alter="greater", conf.int=TRUE, conf.level=0.95)


################################################
# 추론통계분석 - 2-3. 대응 두 집단 평균차이 검정
################################################
# 조건 : A집단  독립적 B집단 -> 비교대상 독립성 유지
# 대응 : 표본이 짝을 이룬다. -> 한 사람에게 2가지 질문
# 사례) 다이어트식품 효능 테스트 : 복용전 몸무게 -> 복용후 몸무게 

# 1. 실습파일 가져오기
getwd()
setwd("c:/Rwork/Part-III")
data <- read.csv("paired_sample.csv", header=TRUE)

# 2. 두 집단 subset 작성

# 1) 데이터 정제
#result <- subset(data, !is.na(after), c(before,after))
dataset <- data[ c('before',  'after')]
dataset

# 2) 적용전과 적용후 분리
before <- dataset$before# 교수법 적용전 점수
after <- dataset$after # 교수법 적용후 점수
before; after

# 3) 기술통계량 
length(before) # 100
length(after) # 100
mean(before) # 5.145
mean(after, na.rm = T) # 6.220833 -> 1.052  정도 증가


# 3. 분포모양 검정 
var.test(before, after, paired=TRUE) 
# 동질성 분포 : t.test()
# 비동질성 분포 : wilcox.test()

# 4. 가설검정
t.test(before, after, paired=TRUE) # p-value < 2.2e-16 

# 방향성이 있는 연구가설 검정 
t.test(before, after, paired=TRUE,alter="greater",conf.int=TRUE, conf.level=0.95) 
#p-value = 1 -> x을 기준으로 비교 : x가 y보다 크지 않다.

#  방향성이 있는 연구가설 검정
t.test(before, after, paired=TRUE,alter="less",conf.int=TRUE, conf.level=0.95) 
# p-value < 2.2e-16 -> x을 기준으로 비교 : x가 y보다 적다.
