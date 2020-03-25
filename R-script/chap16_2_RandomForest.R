##################################################
#randomForest
##################################################
# 결정트리(Decision tree)에서 파생된 모델 
# 랜덤포레스트는 앙상블 학습기법을 사용한 모델
# 앙상블 학습 : 새로운 데이터에 대해서 여러 개의 Tree로 학습한 다음, 
# 학습 결과들을 종합해서 예측하는 모델(PPT 참고)
# DT보다 성능 향상, 과적합 문제를 해결


# 랜덤포레스트 구성방법(2가지)
# 1. 결정 트리를 만들 때 데이터의 일부만을 복원 추출하여 트리 생성 
#  -> 데이터 일부만을 사용해 포레스트 구성 
# 2. 트리의 자식 노드를 나눌때 일부 변수만 적용하여 노드 분류
#  -> 변수 일부만을 사용해 포레스트 구성 
# [해설] 위 2가지 방법을 혼용하여 랜덤하게 Tree(학습데이터)를 구성한다.

# 새로운 데이터 예측 방법
# - 여러 개의 결정트리가 내놓은 예측 결과를 투표방식(voting) 방식으로 선택 


install.packages('randomForest')
library(randomForest) # randomForest()함수 제공 

data(iris)

# 분류 TREE

# 1. 랜덤 포레스트 모델 생성 
# 형식) randomForest(y ~ x, data, ntree, mtry)
model = randomForest(Species~., data=iris)  
# Default parameter
# Number of trees: 500
# No. of variables tried at each split: 2

#node 분할에 사용하는 X변수 갯수
# mtry = sqrt(4) = 2
# 만약 y가 14개인 continous variable이라면
# mtrt = 1/3 * p = 4~5

# 2. 파라미터 조정 300개의 Tree와 4개의 변수 적용 모델 생성 
model = randomForest(Species~., data=iris, 
                     ntree=300, mtry=4, na.action=na.omit )
# Number of trees: 300
# No. of variables tried at each split: 4
model


# 3. 최적의 파리미터(ntree, mtry) 찾기
# - 최적의 분류모델 생성을 위한 파라미터 찾기

ntree <- c(400, 500, 600)
mtry <- c(2:4)

# 2개 vector이용 data frame 생성 
param <- data.frame(n=ntree, m=mtry)
param

for(i in param$n){ # 400,500,600
  cat('ntree = ', i, '\n')
  for(j in param$m){ # 2,3,4
    cat('mtry = ', j, '\n')
    model = randomForest(Species~., data=iris, 
                         ntree=i, mtry=j, 
                         na.action=na.omit )    
    print(model)
  }
}


# 4. 중요 변수 생성  
model3 = randomForest(Species ~ ., data=iris, 
                      ntree=500, mtry=2, 
                      importance = T,
                      na.action=na.omit )
model3 

importance(model3)  
# MeanDecreaseAccuracy MeanDecreaseGini 값이 크면 영향력이 크다.
# MeanDecreaseAccuracy : 분류 정확도 개선에 기여
# MeanDecreaseGini : 노드 불순도(불확실성) = entrophy 개선 기여

varImpPlot(model3)



###################
# 회귀 TREE
###################

library(MASS)
data("Boston")
str(Boston)
#crim : 도시 1인당 범죄율 
#zn : 25,000 평방피트를 초과하는 거주지역 비율
#indus : 비상업지역이 점유하고 있는 토지 비율  
#chas : 찰스강에 대한 더미변수(1:강의 경계 위치, 0:아닌 경우)
#nox : 10ppm 당 농축 일산화질소 
#rm : 주택 1가구당 평균 방의 개수 
#age : 1940년 이전에 건축된 소유주택 비율 
#dis : 5개 보스턴 직업센터까지의 접근성 지수  
#rad : 고속도로 접근성 지수 
#tax : 10,000 달러 당 재산세율 
#ptratio : 도시별 학생/교사 비율 
#black : 자치 도시별 흑인 비율 
#lstat : 하위계층 비율 
#medv(y) : 소유 주택가격 중앙값 (단위 : $1,000)

ntree = 500
p = 13
mtry = 1/3*p
mtry # 4 or 5

boston_model = randomForest(medv~., data=Boston, ntree=ntree ,mtry = mtry , importance = T )
names(boston_model)
boston_model$importance
varImpPlot(boston_model)

y_pred = boston_model$predicted
y_true = boston_model$y
# 표준화(o)
err = y_true - y_pred #잔차
mse = mean(err**2) #10.03818

# 표준화(x)
cor(y_true,y_pred) #0.9419663
# 1 에 가까움으로 매우 상관성이 높다.

# model
# 분류 Tree : confusion matrix
# 회귀 Tree : MSE , Cor 

Titanic <- read.csv('C:\\ITWILL\\2_Rwork\\Part-IV/titanic3.csv', stringsAsFactors = FALSE)

Titanic = Titanic[-c(3,8,10,12,13,14)]
str(Titanic)
dim(Titanic)
Titanic$survived

Titanic$survived = factor(Titanic$survived)

#class(Titanic)
idx = sample(nrow(Titanic), 0.7*nrow(Titanic))
Titanic_train = Titanic[idx, ] # 훈련 데이터 
Titanic_test = Titanic[-idx, ] # 검정 데이터 

model = rpart(survived~., data = Titanic_train)
fancyRpartPlot(model)
model # sex / age pclass / sibsp fare 

Titanic_pred = predict(model, Titanic_test, type = 'class')
Titanic_true = Titanic_test$survived
tab =table(Titanic_true , Titanic_pred)
#     0   1
# 0 204  28
# 1  58 103
acc =  (204+103) / sum(tab)
#0.7811705

####################
# random forest
####################
Titanic2 <- read.csv('C:\\ITWILL\\2_Rwork\\Part-IV/titanic3.csv', stringsAsFactors = FALSE)
Titanic2 = Titanic2[-c(3,8,10,12,13,14)]
str(Titanic2)
dim(Titanic2)
Titanic2$survived

Titanic2$survived = factor(Titanic2$survived)

class(Titanic2)
str(Titanic2)
mtry = round(sqrt(7))
ntree=500
table(is.na(Titanic2))

model = randomForest(survived~., data=Titanic2, ntree=500 ,mtry = 3 , 
                     importance = T,
                     na.action=na.omit)

varImpPlot(model)
importance(model)
#Humidity3pm



###########################
# Entrophy : 불확실성 척도
###########################
# - Tree Model에서 중요 변수 선정 기준

# EX1)
# x1 : 앞면 , x2 : 뒷면
# 불확실성이 가장 높은 경우 -> 2개 다 50% 50%인 경우
x1=0.5
x2=0.5

e1 = -x1*log2(x1) -x2*log2(x2)
exp(1) #2.718282
e1 # 1
#entropy 가 1인 경우가 제일 불확실성이 큰 경우이다.


# EX2)
# x1 = 0.8 x2 = 0.2
x1=0.8
x2=0.2
e2 = -x1*log2(x1) -x2*log2(x2)
e2 #0.7219281
