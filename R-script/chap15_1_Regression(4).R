###################################
# 3. 다중공선성(Multicolinearity)
###################################
# - 독립변수 간의 강한 상관관계로 인해서 회귀분석의 결과를 신뢰할 수 없는 현상
# - 생년월일과 나이를 독립변수로 갖는 경우
# - 해결방안 : 강한 상관관계를 갖는 독립변수 제거

# (1) 다중공선성 문제 확인
library(car)
fit <- lm(formula=Sepal.Length ~ Sepal.Width+Petal.Length+Petal.Width, data=iris)
vif(fit)
sqrt(vif(fit))>2 # root(VIF)가 2 이상인 것은 다중공선성 문제 의심 

# (2) iris 변수 간의 상관계수 구하기
cor(iris[,-5]) # 변수간의 상관계수 보기(Species 제외) 
#x변수 들끼 계수값이 높을 수도 있다. -> 해당 변수 제거(모형 수정) <- Petal.Width

# (3) 학습데이터와 검정데이터 분류
nrow(iris)#150
x <- sample(1:nrow(iris), 0.7*nrow(iris)) # 전체중 70%만 추출
train <- iris[x, ] # 학습데이터 추출
test <- iris[-x, ] # 검정데이터 추출

# (4) Petal.Width 변수를 제거한 후 회귀분석 
iris_model <- lm(formula=Sepal.Length ~ Sepal.Width + Petal.Length, data=train)
iris_model
summary(result.lm)

# (5) model 예측치 : test
y_pred = predict(iris_model , test)
length(y_pred)

# (6) model 평가  
# MSE(표준화 o )
y_true = test$Sepal.Length
Error = y_true - y_pred
mse = mean(Error**2)
mse #0.1170933  / 0 에 가까울수록 오차가 적다.

#상관 계수 평가 (표준화 x)
r = cor(y_true,y_pred)
r # 0.895351 / 1에 가까워야 차이가 적다. 

#시각화 평가
plot(y_true,col='blue',type='l',label='y true')
points(y_pred,col='red',type='l',label='y pred')
legend("topleft",legend=c('y true', 'y pred'),col=c('blue','red'),pch='-')

