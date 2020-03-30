##########################
## 제17-3장 SVM 연습문제 
##########################

# 문1) 기상데이터를 다음과 같이 SVM에 적용하여 분류하시오. 
# 조건1> 포물라 적용 : RainTomorrow ~ .  
# 조건2> kernel='radial', kernel='linear' 각 model 생성 및 평가 비교 

# 1. 파일 가져오기 
weatherAUS = read.csv(file.choose()) #weatherAUS.csv
weatherAUS = weatherAUS[ ,c(-1,-2, -22, -23)] # 칼럼 제외 
str(weatherAUS)

# 2. 데이터 셋 생성 
set.seed(415)
idx = sample(1:nrow(weatherAUS), 0.7*nrow(weatherAUS))
training_w = weatherAUS[idx, ]
training_w  = na.omit(training_w)
testing_w  = weatherAUS[-idx, ]
testing_w  = na.omit(testing_w)
dim(training_w)
dim(testing_w)
# 3. 분류모델 생성 : kernel='radial', kernel='linear' 
model_wea = svm(RainTomorrow ~ ., data = training_w, na.action =na.omit)

# 4. 분류모델 평가 
pred <- predict(model_wea, testing_w)
tab = table(pred,testing_w$RainTomorrow)

# pred    No  Yes
# No    3894  601
# Yes   179  619
(tab[1,1]+tab[2,2]) / sum(tab)

# 문2) 문1에서 생성한 모델을 tuning하여 최적의 모델을 생성하시오.
params = c(0.001,0.01,0.1,1,10,100,1000)
tuning = tune.svm(RainTomorrow ~ ., data = training_w,
                  gamma = params , cost = params)



