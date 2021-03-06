#Decision tree

library(rpart) # rpart() : 분류모델 생성 
install.packages("rpart.plot")
library(rpart.plot) # prp(), rpart.plot() : rpart 시각화
install.packages('rattle')
library('rattle') # fancyRpartPlot() : node 번호 시각화 


# 단계1. 실습데이터 생성 
data(iris)
set.seed(415)
idx = sample(1:nrow(iris), 0.7*nrow(iris))
train = iris[idx, ]
test = iris[-idx, ]
dim(train) # 105 5
dim(test) # 45  5

table(train$Species)

# 단계2. 분류모델 생성 
# rpart(y변수 ~ x변수, data)
model = rpart(Species~., data=train) # iris의 꽃의 종류(Species) 분류 
model

# 분류모델 시각화 - rpart.plot 패키지 제공 
prp(model) # 간단한 시각화   
rpart.plot(model) # rpart 모델 tree 출력
fancyRpartPlot(model) # node 번호 출력(rattle 패키지 제공)

##########################
# 가지치기(cp)
##########################
# Tree의 가지치기 : 과적합 문제 해결법
# cp : 0 ~ 1 , default = 0.05
# 0으로 갈수록 트리 커짐 , 오류율 감소 , 과적합 증가
model$cp
#     CP nsplit  rel error     xerror       xstd
# 1 0.5147059      0 1.00000000 1.11764706 0.06737554
# 2 0.4558824      1 0.48529412 0.57352941 0.07281162
# 3 0.0100000      2 0.02941176 0.02941176 0.02059824
# xstd(오류율) 3번이 가장 적은 오류율을 가지고 있다.
# 3번이 과적합 발생 -> 0.45 조정정

# 단계3. 분류모델 평가  
pred <- predict(model, test) # 비율 예측 
pred <- predict(model, test, type="class") # 분류 예측 

# 1) 분류모델로 분류된 y변수 보기 
tab = table(pred)

# 2) 분류모델 성능 평가 
table(pred, test$Species)
sum=0
for(i in 1:3){
  sum = sum+ tab[i,i]
}
sum/nrow(test)
