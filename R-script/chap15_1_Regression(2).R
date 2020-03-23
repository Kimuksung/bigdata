###################################
## 2. 다중회귀분석
###################################
# - 여러 개의 독립변수 -> 종속변수에 미치는 영향 분석
# 가설 : 음료수 제품의 적절성(x1)과 친밀도(x2)는 제품 만족도(y)에 정의 영향을 미친다.

product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)


#(1) 적절성 + 친밀도 -> 만족도  
y = product$'제품_만족도' # 종속변수
x1 = product$'제품_친밀도' # 독립변수1
x2 = product$'제품_적절성' # 독립변수2

df <- data.frame(x1, x2, y)

result.lm <- lm(formula=y ~ x1 + x2, data=df)
#result.lm <- lm(formula=y ~ ., data=df)

# 계수 확인 
result.lm
b = 0.66731
a1 = 0.09593
a2 = 0.68522
x1 = 3 
x2 = 4 

#다중 회귀 방정식
y=a1*x1+a2*x2 + b
Y = 3
err = Y-y
abs(err)

summary(result.lm)

# F-statistic p-value: < 2.2e-16
# Adjusted R-squared:  0.5945 
# x의 유의성 검정
# x1            2.478   0.0138 *      -> 친밀도  
# x2           15.684  < 2e-16 ***    -> 적절성
# 적절성이 고객 만족도에 더 많은 영향을 끼친다.