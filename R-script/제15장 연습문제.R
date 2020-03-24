#################################
## <제15장 연습문제>
################################# 

###################################
## 선형 회귀분석 연습문제 
###################################

# 01. ggplot2패키지에서 제공하는 diamonds 데이터 셋을 대상으로 
# carat, table, depth 변수 중 다이아몬드의 가격(price)에 영향을 
# 미치는 관계를 다음과 같은 단계로 다중회귀분석을 수행하시오.

library(ggplot2)
data(diamonds)


# 단계1 : 다이아몬드 가격 결정에 가장 큰 영향을 미치는 변수는?
str(diamonds)
y= diamonds$price
x1 = diamonds$carat
x2 = diamonds$table
x3 = diamonds$depth

df <- data.frame(x1, x2, x3, y)
result.lm <- lm(formula=y ~ x1 + x2 + x3, data=df)
summary(result.lm)
# 
#             Estimate Std. Error t value
# (Intercept) 13003.441    390.918   33.26
# x1           7858.771     14.151  555.36
# x2           -104.473      3.141  -33.26
# x3           -151.236      4.820  -31.38

# 단계2 : 다중회귀 분석 결과를 정(+)과 부(-) 관계로 해설
# depth table 부  carat 정

# 02. mtcars 데이터셋을 이용하여 다음과 같은 단계로 다중회귀분석을 수행하시오.

library(datasets)
str(mtcars) # 연비 효율 data set 


# 단계1 : 연비(mpg)는 마력(hp), 무게(wt) 변수와 어떤 상관관계를 갖는가? 
y = mtcars$mpg
x1 = mtcars$hp
x2 = mtcars$wt

df <- data.frame(x1, x2, y)
cor(df)
#result.lm <- lm(formula=y ~ x1 + x2, data=df)

summary(result.lm)
# 단계2 : 마력(hp)과 무게(wt)는 연비(mpg)에 어떤 영향을 미치는가? 
#                               t value
# 마력           0.00145 **     -3.519
# 무게          1.12e-06 ***    -6.129


# 단계3 : hp = 90, wt = 2.5t일 때 회귀모델의 예측치는?
x_data = data.frame(x1=90,x2=2.5)
y_pred = predict(df,x_data)
y_pred


# 03. product.csv 파일의 데이터를 이용하여 다음과 같은 단계로 다중회귀분석을 수행하시오.
setwd("D:/ITWILL/2_Rwork/Part-IV")
product <- read.csv("product.csv", header=TRUE)
str(product)
predict(result.lm, data.frame(x=5) ) 
#  단계1 : 학습데이터(train),검정데이터(test)를 7 : 3 비율로 샘플링
temp <- sample(1:nrow(product), 0.7*nrow(product),replace=F) #비복원 추출
train <- product[temp,] # 학습데이터 추출
test <- product[-temp, ] # 검정데이터 추출
dim(test)
dim(train)

#  단계2 : 학습데이터 이용 회귀모델 생성 
#        변수 모델링) y변수 : 제품_만족도, x변수 : 제품_적절성, 제품_친밀도
product_model <- lm(formula=제품_만족도 ~ 제품_적절성 
                    + 제품_친밀도, data=train)


#  단계3 : 검정데이터 이용 모델 예측치 생성 
y_pred = predict(product_model , test)
length(y_pred)
#  단계4 : 모델 평가 : cor()함수 이용  
y_true = test$'제품_만족도'
r = cor(y_true,y_pred)
r
###################################
## 로지스틱 회귀분석 연습문제 
###################################
# 04.  admit 객체를 대상으로 다음과 같이 로지스틱 회귀분석을 수행하시오.
# <조건1> 변수 모델링 : y변수 : admit, x변수 : gre, gpa, rank 
# <조건2> 7:3비율로 데이터셋을 구성하여 모델과 예측치 생성 
# <조건3> 분류 정확도 구하기 

# 파일 불러오기
admit = read.csv(choose.files())
admit <- read.csv('admit.csv')
str(admit) # 'data.frame':	400 obs. of  4 variables:
#$ admit: 입학여부 - int  0 1 1 1 0 1 1 0 1 0 ...
#$ gre  : 시험점수 - int  380 660 800 640 520 760 560 400 540 700 ...
#$ gpa  : 시험점수 - num  3.61 3.67 4 3.19 2.93 3 2.98 3.08 3.39 3.92 ...
#$ rank : 학교등급 - int  3 3 1 4 4 2 1 2 3 2 ...

# 1. data set 구성 
idx <- sample(1:nrow(admit), nrow(admit)*0.7)
train_admit <- admit[idx, ]
test_admit <- admit[-idx, ]

# 2. model 생성 
admit_model=glm(admit ~ ., data = train_admit, family = 'binomial')

# 3. predict 생성 
admit_pred = predict(admit_model, newdata=test_admit, type="response")
y_pred = ifelse(admit_pred>=0.5,1,0)
x_true = test_admit$admit
# 4. 모델 평가(분류정확도) : 혼돈 matrix 이용/ROC Curve 이용
tab = table(x_true , y_pred)
tab

acc = (tab[1,1]+tab[2,2]/sum(tab))
acc

library(ROCR)
pr <- prediction(admit_pred, test_admit$admit)
prf <- performance(pr, measure = "tpr", x.measure = "fpr")
plot(prf)

