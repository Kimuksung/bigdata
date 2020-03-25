##################################################
# Decision Tree 응용실습 : 암 진단 분류 분석
##################################################
# "wdbc_data.csv" : 유방암 진단결과 데이터 셋 분류

# 1. 데이터셋 가져오기 
wdbc <- read.csv('C:\\ITWILL\\2_Rwork\\Part-IV/wdbc_data.csv', stringsAsFactors = FALSE)
str(wdbc)

# 2. 데이터 탐색 및 전처리 
wdbc <- wdbc[-1] # id 칼럼 제외(이상치) 
head(wdbc)
head(wdbc[, c('diagnosis')], 10) # 진단결과 : B -> '양성', M -> '악성'

# 목표변수(y변수)를 factor형으로 변환 
wdbc$diagnosis <- factor(wdbc$diagnosis, levels = c("B", "M"))#B -base
wdbc$diagnosis[1:10]

# 3. 정규화  : 서로 다른 특징을 갖는 칼럼값 균등하게 적용 
normalize <- function(x){ # 정규화를 위한 함수 정의 
  return ((x - min(x)) / (max(x) - min(x)))
}

# wdbc[2:31] : x변수에 해당한 칼럼 대상 정규화 수행 
wdbc_x <- as.data.frame(lapply(wdbc[2:31], normalize))
wdbc_x
summary(wdbc_x) # 0 ~ 1 사이 정규화 
class(wdbc_x) # [1] "data.frame"
nrow(wdbc_x) # [1] 569

wdbc_df <- data.frame(wdbc$diagnosis, wdbc_x)
dim(wdbc_df) # 569  31
head(wdbc_df)

# 4. 훈련데이터와 검정데이터 생성 : 7 : 3 비율 
idx = sample(nrow(wdbc_df), 0.7*nrow(wdbc_df))
wdbc_train = wdbc_df[idx, ] # 훈련 데이터 
wdbc_test = wdbc_df[-idx, ] # 검정 데이터 


# 5. rpart 분류모델 생성 
model = rpart(wdbc.diagnosis~., data = wdbc_train)
model
fancyRpartPlot(model)

# 6. 분류모델 평가  
y_pred = predict(model, wdbc_test,type = 'class')
#y_pred = predict(model, wdbc_test)
#y_pred =iflese(y_pred[,1]>=0.5, 0,1)
head(y_pred[,1])
y_true = wdbc_test$wdbc.diagnosis
table(y_true , y_pred)
# B 112   3
# M  11  45
acc = (112+45) / nrow(wdbc_test)
# 0.9181287
M = 45 / (11+45)
# 0.8035714

B = 112 / (112+3)
# 0.973913

###########################
# 교차검정
###########################

# 1단계 : k겹 교차 검정을 위한 sampling
install.packages("cvTools")
library(cvTools)

cross = cvFolds(n=nrow(iris), K = 3 , R =1 ,type='random')
#n=150 
# K3 :3 -> d1 : 50, d2 : 50 ,d3 : 50
cross
str(cross)

# set1
d1 = cross$subsets[cross$which==1,1]
# set2
d2 = cross$subsets[cross$which==2,1]
# set3
d3 = cross$subsets[cross$which==3,1]

K = 1:3
R =1
acc = numeric()
for(r in R){ # 열의 indexing
  for(k in K){ # k겹
    idx = cross$subsets[cross$which==k,r]
    # cat('k=',k,'\n')
    # print(idx)
    test = iris[idx,]
    train = iris[-idx,]
    model = rpart(Species~., data=train)
    pred=predict(model, test, type='class')
    tab = table(test$Species,pred) #교차 분할표
    acc[k] = (tab[1,1]+tab[2,2]+tab[3,3])/sum(tab)    
    }
}
acc # 0.92 0.94 0.94
mean(acc)

# titanic3.csv 변수 설명
#'data.frame': 1309 obs. of 14 variables:
#1.pclass : 1, 2, 3등석 정보를 각각 1, 2, 3으로 저장
#2.survived : 생존 여부. survived(생존=1), dead(사망=0)
#3.name : 이름(제외)
#4.sex : 성별. female(여성), male(남성)
#5.age : 나이
#6.sibsp : 함께 탑승한 형제 또는 배우자의 수
#7.parch : 함께 탑승한 부모 또는 자녀의 수
#8.ticket : 티켓 번호(제외)
#9.fare : 티켓 요금
#10.cabin : 선실 번호(제외)
#11.embarked : 탑승한 곳. C(Cherbourg), Q(Queenstown), S(Southampton)
#12.boat     : (제외)Factor w/ 28 levels "","1","10","11",..: 13 4 1 1 1 14 3 1 28 1 ...
#13.body     : (제외)int  NA NA NA 135 NA NA NA NA NA 22 ...
#14.home.dest: (제외)

Titanic <- read.csv('C:\\ITWILL\\2_Rwork\\Part-IV/titanic3.csv', stringsAsFactors = FALSE)


# 조건1> 6개 변수 제외 -> subset 생성
# 조건2> survived : int -> factor 변환 (0 : 사망 ,1 : 생존)
# 조건3> train test 7:3
# 조건4> 생존 여부에 가장 중요한 변수?
# 조건5> model 평가 ( 분류 정확도 )

Titanic = Titanic[-c(3,8,10,12,13,14)]
str(Titanic)
dim(Titanic)
Titanic$survived

temp <- factor(Titanic$survived, levels = c("Dead", "Survive"))
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


