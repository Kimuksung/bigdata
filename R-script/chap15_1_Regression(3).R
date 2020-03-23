install.packages('car')
library(car)

Prestige # 직업군에 관련된 평판
str(Prestige)
# $ education: 교육수준 x1
# $ income   : 수입 y
# $ women    : 여성 비율 x2
# $ prestige : 평판 x3
# $ census   : 직업수
# $ type     : factor

row.names(Prestige)

df = Prestige[,c(1:4)]
model1 = lm(formula = income~., data = df)

summary(model1)

# education    177.199    187.632
# women        -50.896      8.556
# prestige     141.435     29.910
res =model1$residuals # 잔차( 오차 ) = 정답 - 예측지
res

#잔차 표준화
res_scale = scale(res)
shapiro.test(res) # p-value = 1.816e-11< 0.05 정규분포

#MSE
mse= mean(res**2) #평균제곱 오차
mse= mean(res_scale**2) #표준화 후 
# 제곱 : 부호 절대값 , 패널티
# 평균 : 전체 오차에 대한 평균

###############################Q###
## 3. x 변수 선택
####################################

new_data = Prestige[,c(1:5)]

library(Math)
library(MASS)

dim( new_data)

model2=lm(income~.,data=new_data)

step = stepAIC(model2,direction='both')#income ~ women + prestige
model3 = lm(income~women+prestige,data=new_data)

summary(model3)
# Adjusted R-squared:  0.6327 
# 0.6323 -> 0.6327

  
