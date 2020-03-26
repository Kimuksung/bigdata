# xgboost vs randomForest
# - xgboost : boosting 방식 
# - randomForest : bagging 방식 

# 1. package install
install.packages("xgboost")
library(xgboost)
#library(help="xgboost")

# 2. dataset load/search
data(agaricus.train)
data(agaricus.test)

train <- agaricus.train
test <- agaricus.test

str(train)
train$data@Dim #6513  126
# class -> object
# $data : $ = key , @ = member(slot) matrix
# $label = y 변수 vector : [1:6513] 
str(test)

train$data
class(train$data)
str(train)
train$label
table(train$label)
# 0    1 
# 3373 3140 

# 3. xgboost matrix 생성 : 객체 정보 확인  
#dtrain = xgb.DMatrix(data=x, label=y)
dtrain <- xgb.DMatrix(data = train$data, label = train$label) # x:data, y:label
dtrain 

?xgboost
#We will train decision tree model using the following parameters:
# •objective = "binary:logistic": we will train a binary classification model ;
# "binary:logistic" : y변수 이항 
# •max_depth = 2: the trees won't be deep, because our case is very simple ;
# tree 구조가 간단한 경우 : 2
# •nthread = 2: the number of cpu threads we are going to use;
# cpu 사용 수 : 2
# •nrounds = 2: there will be two passes on the data, the second one will enhance the model by further reducing the difference between ground truth and prediction.
# 실제값과 예측값의 차이를 줄이기 위한 반복학습 횟수 
# •eta = 1 : eta control the learning rate 
# 학습률을 제어하는 변수(Default: 0.3) 
# 숫자가 낮을 수록 모델의 복잡도가 높아지고, 컴퓨팅 파워가 더많이 소요
# 부스팅 과정을보다 일반화하여 오버 피팅을 방지하는 데 사용
# •verbose = 0 : no message
# 0이면 no message, 1이면 성능에 대한 정보 인쇄, 2이면 몇 가지 추가 정보 인쇄

# 4. model 생성 : xgboost matrix 객체 이용  
xgb_model <- xgboost(data = dtrain, max_depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic", verbose = 0)

# 5.  학습된 model의 변수(feature) 중요도/영향력 보기 
import <- xgb.importance(colnames(train$data), model = xgb_model)
import
xgb.plot.importance(importance_matrix = import)

# 6. 예측치
pred = predict(xgb_model , test$data)
range(pred)

y_pred = ifelse(pred >= 0.5 , 1, 0)
y_true = test$label
tab = table(y_true , y_pred)
tab

# 7. 모델 평가
# 1) 분류 정확도
acc = (tab[1,1] + tab[2,2]) / length(y_true)
# 0.9782744

# 2) 평균 오차
mean_err = mean(as.numeric(pred >= 0.5) != y_true)
# 0.02172564

# 8. model save & model load

# 1) model file save
setwd("C:\\ITWILL\\2_Rwork\\output")
xgb.save(xgb_model, 'xgboost.model') # (obj , filename)
# [1] TRUE

rm(list = ls())

# 2) model load(memory loading)
xgb_model2 = xgb.load('xgboost.model')

pred2 = predict(xgb_model2,test$data)
range(pred2)

##############################
# iris dataset : y = 이항분류#
##############################
iris_df = iris

# 1. y 변수 -> binary
iris_df$Species = ifelse(iris_df$Species=='setosa',0,1)
str(iris_df)
table(iris_df$Species)

# 2. dataset 생성
idx = sample(nrow(iris_df),nrow(iris_df)*0.7)
train = iris_df[idx,]
test = iris_df[-idx,]

# 3. Dmatrix 생성
# x : matrix , y : vector
train_x = as.matrix(train[,-5])
train_y = train[,5]

dtrain = xgb.DMatrix(data = train_x , label=train_y)
dtrain

# 4. xgboost model 생성 과정
xgb_iris_model <- xgboost(data = dtrain, max_depth = 2, eta = 1, nthread = 2, nrounds = 2, objective = "binary:logistic", verbose = 0)
import <- xgb.importance(colnames(train_x), model = xgb_iris_model)
xgb.plot.importance(importance_matrix = import)

# 5. 예측치
pred = predict(xgb_iris_model,as.matrix(test[,-5]))
range(pred) # 0.06361979 0.94918537

y_pred = ifelse(pred >= 0.5,1,0)
tab = table(test[,5],y_pred)
acc = (tab[1,1]+tab[2,2])/ length(test[,5])
acc

