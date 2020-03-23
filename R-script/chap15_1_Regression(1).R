######################################################
# 회귀분석(Regression Analysis)
######################################################
# - 특정 변수(독립변수:설명변수)가 다른 변수(종속변수:반응변수)에 어떠한 영향을 미치는가 분석

###################################
## 1. 단순회귀분석 
###################################
# - 독립변수와 종속변수가 1개인 경우

# 단순선형회귀 모델 생성  
# 형식) lm(formula= y ~ x 변수, data) 
setwd("C:\\ITWILL\\2_Rwork\\Part-IV")
product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)

str(product) # 'data.frame':  264 obs. of  3 variables:
y = product$제품_만족도 # 종속변수
x = product$제품_적절성 # 독립변수
df <- data.frame(x, y)
df
# 회귀모델 생성 
result.lm <- lm(formula=y ~ x, data=df) # formula 종속 변수 ~ 독립변수
result.lm # 회귀계수 


# Coefficients:
#   (Intercept)            x  
# 0.7789       0.7393  

#회귀 방정식(y) = a.x + b   a: 기울기 b: 절편


head(df)
X=4 # 입력 변수
Y=3 # 정답
a=0.7393

# 회귀 방정식 : y 예측치
b=0.7789
y = a*X+b

#Y = 3.7361
err = y-Y
err

names(result.lm)
# "coefficients" : 회귀 계수
# "residuals" : 오차(잔차)
# "fitted.values" : 적합치(예측치)
result.lm$coefficients
result.lm$residuals
result.lm$fitted.values

# 회귀모델 예측 
# predict(model,x)
predict(result.lm, data.frame(x=5) ) 
# (2) 선형회귀 분석 결과 보기
summary(result.lm)
#< 회귀 모델 해석 순서>
# 1. F-statistic : p-value <0.05 이면 통계적으로 유효하다.
# 2. Adjusted R-squared:  0.5865 - 설명력(예측력) 1에 가까울 수록 예측력이 높은것.
# 3. X의 유의성 검정 : t-value , p-value 
# Signif. codes : 0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05

r = cor(df)
#r 설명력 = r**2



# (3) 단순선형회귀 시각화
# x,y 산점도 그리기 
plot(formula=y ~ x, data=df)
# 회귀분석
result.lm <- lm(formula=y ~ x, data=df)
# 회귀선 
abline(result.lm, col='red')

result.lm$coefficients
# 0.7788583 x= 0.7392762

y = product$제품_만족도
x = product$제품_적절성

# 기울기 = covxy / sxx
covxy = mean((x - mean(x)) * ( y-mean(y)))
sxx = mean((x-mean(x))**2)
a = covxy /sxx
a
# y절편
b= mean(y) - (a*mean(x))
b


