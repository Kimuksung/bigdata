# chap13_Ttest_Anova(연습문제)

#############################################
# 추론통계분석 - 1-1. 단일집단 비율차이 검정
#############################################

# 01. 중소기업에서 생산한 HDTV 판매율을 높이기 위해서 프로모션을 진행한 결과 
# 기존 구매비율 15% 보다 향상되었는지를 각 단계별로 분석을 수행하여 검정하시오.


#연구가설(H1) : 기존 구매비율과 차이가 있다.
#귀무가설(H0) : 기존 구매비율과 차이가 없다.

#조건) 구매여부 변수 : buy (1: 구매하지 않음, 2: 구매)

#기존 구매 비율 old / 신규 구매 비율 new
#(1) 데이터셋 가져오기
setwd("C:/ITWILL/2_Rwork/Part-III")
hdtv <- read.csv("hdtv.csv", header=TRUE)
head(hdtv)
# (2) 빈도수와 비율 계산
table(hdtv$buy)
prop.table(table(hdtv$buy))
# (3)가설검정
#binom.test(성공횟수, 시행횟수, p = 확률)
binom.test(10, 50, p=0.15)
# p-value = 0.321 > 0.05 이기 때문에 차이가 없다.


#################################################
# 추론통계학 분석 - 1-2. 단일집단 평균차이 검정
#################################################

# 02. 우리나라 전체 중학교 2학년 여학생 평균 키가 148.5cm로 알려져 있는 상태에서 
# A중학교 2학년 전체 500명을 대상으로 10%인 50명을 표본으로 선정된 데이터 셋을 이용하여
# 모집단의 평균과 차이가 있는지를 각 단계별로 분석을 수행하여 검정하시오.

#(1) 데이터셋 가져오기
sheight<- read.csv("student_height.csv", header=TRUE)
dim(sheight)

# (2) 기술통계량 평균 계산
mean(sheight$height)

# (3) 정규성 검정
shapiro.test(sheight$height)
# W = 0.88711, p-value = 0.0001853

# (4) 가설검정 
wilcox.test(sheight$height,mu=148.5)
# p-value = 0.067> 0.05 차이가 없다.

#################################################
# 추론통계학 분석 - 2-1. 두집단 비율 차이 검정
#################################################

# 03. 대학에 진학한 남학생과 여학생을 대상으로 진학한 대학에 
# 대해서 만족도에 차이가 있는가를 검정하시오.

# 힌트) 두 집단 비율 차이 검정
#  조건) 파일명 : two_sample.csv, 변수명 : gender(1,2), survey(0,1)
# gender : 남학생(1), 여학생(2)
# survey : 불만(0), 만족(1)
# prop.test('성공횟수', '시행횟수')
temp = read.csv("two_sample.csv")
head(temp)
temp$gender2[temp$gender==1]="남학생"
temp$gender2[temp$gender==2]="여학생"
temp$survey2[temp$survey==0]="불만"
temp$survey2[temp$survey==1]="만족"

temp2 = subset(temp,!is.na(gender2),c(gender2,survey2)) 
head(temp2)
table(temp2$gender)
table(temp2$survey)
table(temp2$gender, temp2$survey, useNA="ifany") 

prop.test(c(138,107),c(174,126))
prop.test(c(36,107),c(174,126))

##################################################
# 추론통계학 분석 - 2-2. 두집단 평균 차이 검정
##################################################

# 04. 교육방법에 따라 시험성적에 차이가 있는지 검정하시오.

#힌트) 두 집단 평균 차이 검정
#조건1) 파일 : twomethod.csv
#조건2) 변수 : method : 교육방법, score : 시험성적
#조건3) 모델 : 교육방법(명목)  ->  시험성적(비율)
#조건4) 전처리 : 결측치 제거 : 평균으로 대체 

temp3 = read.csv("twomethod.csv")
str(temp3)
head(temp3)
temp4 = subset(temp3,!is.na(score),c(method,score)) 
method1 <- subset(temp4, method==1)
method2 <- subset(temp4, method==2)

mean(method1$score)
mean(method2$score)

var.test(method1$score, method2$score)
#p-value = 0.8494 -> 동질성 분포 : t.test()

t.test(method1_score, method2_score)
#약간의 차이가 있다.



# 05. iris dataset을 이용하여 분산 분석으로 수행하시오.
iris
# 독립 변수 : Species(집단 변수)
# 종속 변수 : 전제조건을 마족하는 변수(1~4 칼럼) 선택
# Sepal.Length Sepal.Width Petal.Length Petal.Width
# 분산 분석 수행 -> 사후 검정
Species = iris$Species
table(Species, useNA="ifany")
table(method, Sepal.Width , useNA="ifany")

summary(iris)
plot(iris$Sepal.Width)
boxplot(iris$Sepal.Width)$stats
mean(iris$Sepal.Width)

boxplot(iris$Sepal.Width)$stats

# 동질성 검정
bartlett.test(Sepal.Length ~Species , data=iris)
#p-value 0.0003345 x

bartlett.test(Sepal.Width ~Species , data=iris)
#p-value 0.3515 o 

result <- aov(Sepal.Width ~Species , data=iris)
summary(result) 
#p-value < 0.05종에 따라 적어도 한집단의 평균 width 의 차이가 있다.

TukeyHSD(result) 
#virginica-versicolor은 큰차이를 보인다.

plot(TukeyHSD(result))

library(dplyr)

iris %>% group_by(Species) %>% summarise(age = mean(Sepal.Width))
