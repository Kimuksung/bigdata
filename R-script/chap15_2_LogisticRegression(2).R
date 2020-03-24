# 다항형 로지스틱 회귀분석 : nnet

install.packages('nnet')
library(nnet)

idx = sample(nrow(iris),nrow(iris)*0.7)
train = iris[idx,]
test = iris[-idx,]

# 활성함수 
# 이항 : sigmoid function - 0~1의 확률값
# 다항 : softmax function - 0~1의 확률값(sum=1)
# y1=0.1 y2=0.1 y3=0.8 
# x1 .. xn -> Model -> y1 , y2 , y3 
# yn 개 중에서 가장 높은 값 추출

names(iris)
model = multinom(Species~., data=train) #다항 분류에 적합한 modeling
model

# x1 , x2 , x3, x4-> Hidden layer(18개) - y1 ,y2 , y3
names(model)
model$fitted.values
range(model$fitted.values)
#1.838885e-34 ~ 1.000000e+00
str(model$fitted.values)
#[1:105, 1:3]
model$fitted.values[1,] #setosa 예측치

train[1,] #setosa 실제 관측치

# 예측치
y_pred = predict(model, test)

y_true = test$Species

#교차 분할표(confusion matrix)
tab = table(y_true,y_pred)
# 43 /45

acc = (tab[1,1] + tab[2,2] + tab[3,3]) / nrow(test)
acc
# 0.9555556


