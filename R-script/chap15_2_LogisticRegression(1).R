###############################################
# 15_2. 로지스틱 회귀분석(Logistic Regression) 
###############################################

# 목적 : 일반 회귀분석과 동일하게 종속변수와 독립변수 간의 관계를 나타내어 
# 향후 예측 모델을 생성하는데 있다.

# 차이점 : 종속변수가 범주형 데이터를 대상으로 하며 입력 데이터가 주어졌을 때
# 해당 데이터의결과가 특정 분류로 나눠지기 때문에 분류분석 방법으로 분류된다.
# 유형 : 이항형(종속변수가 2개 범주-Yes/No), 다항형(종속변수가 3개 이상 범주-iris 꽃 종류)
# 다항형 로지스틱 회귀분석 : nnet, rpart 패키지 이용 
# a : 0.6,  b:0.3,  c:0.1 -> a 분류 

# 분야 : 의료, 통신, 기타 데이터마이닝

# 선형회귀분석 vs 로지스틱 회귀분석 
# 1. 로지스틱 회귀분석 결과는 0과 1로 나타난다.(이항형)
# 2. 정규분포 대신에 이항분포를 따른다.
# 3. 로직스틱 모형 적용 : 변수[-무한대, +무한대] -> 변수[0,1]사이에 있도록 하는 모형 
#    -> 로짓변환 : 출력범위를 [0,1]로 조정
# 4. 종속변수가 2개 이상인 경우 더미변수(dummy variable)로 변환하여 0과 1를 갖도록한다.
#    예) 혈액형 AB인 경우 -> [1,0,0,0] AB(1) -> A,B,O(0)


# 단계1. 데이터 가져오기
weather = read.csv("C:/ITWILL/2_Rwork/Part-IV/weather.csv", stringsAsFactors = F) 
dim(weather)  # 366  15
head(weather)
str(weather)

# chr 칼럼, Date, RainToday 칼럼 제거 
weather_df <- weather[, c(-1, -6, -8, -14)]
str(weather_df)

# RainTomorrow 칼럼 -> 로지스틱 회귀분석 결과(0,1)에 맞게 더미변수 생성      
weather_df$RainTomorrow[weather_df$RainTomorrow=='Yes'] <- 1
weather_df$RainTomorrow[weather_df$RainTomorrow=='No'] <- 0
weather_df$RainTomorrow <- as.numeric(weather_df$RainTomorrow)
head(weather_df)

#y 빈도수
table(weather_df$RainTomorrow)
prop.table(table(weather_df$RainTomorrow))
#     0         1 
# 0.8196721 0.1803279 


#  단계2.  데이터 셈플링
idx <- sample(1:nrow(weather_df), nrow(weather_df)*0.7)
train <- weather_df[idx, ]
test <- weather_df[-idx, ]


#  단계3.  로지스틱  회귀모델 생성 : 학습데이터 
weater_model <- glm(RainTomorrow ~ ., data = train, family = 'binomial')
weater_model 
summary(weater_model) 


# 단계4. 로지스틱  회귀모델 예측치 생성 : 검정데이터 
# newdata=test : 새로운 데이터 셋, type="response" : 0~1 확률값으로 예측 
pred <- predict(weater_model, newdata=test, type="response")  #sigmoid
pred 
range(pred,na.rm=T)#0.0008055924 0.9982066277
summary(pred)
str(pred)
#$cut off = 0.5
cpred = ifelse(pred>= 0.5,1,0)
table(cpred)


# 단계 5 : 모델 평가
y_true = test$RainTomorrow
# 교차분할표 
tab=table(y_true,cpred)
#           cpred
# y_true      0  1
#         0   79  8
#         1   8 12


# 정분류 : 분류 정확도
#비오기 전날 예측
acc = (79+12) / nrow(test)
acc # 0.8272727

yes = 7/(8+12)
yes # 0.3181818

yes = 79/(79+8)
yes

# 특이도 : 관측치(No) -> No
tab[1,1] / (tab[1,1]+tab[1,2]) #0.9

# 민감도(재현율)  : 관측치(YES) -> YES
recall = tab[2,2] / (tab[2,1]+tab[2,2])
recall # 0.6111111

# 정확률 : 예측치(yes) -> yes 
precision = tab[2,2] / (tab[1,2] + tab[2,2])
precision #0.55

# 6) F1_score : 불균형 비율   ->  종합 적으로 판단한 결과 57%
F1_score = 2*((recall*precision) / (recall + precision))
# 0.5789474


### ROC Curve를 이용한 모형평가(분류정확도)  ####
# Receiver Operating Characteristic

install.packages("ROCR")
library(ROCR)

# ROCR 패키지 제공 함수 : prediction() -> performance
pr <- prediction(pred, test$RainTomorrow)
prf <- performance(pr, measure = "tpr", x.measure = "fpr")
plot(prf)


############################
## 6. 범주형 X 변수 사용
############################

# 범주형 변수 -> 더미 변수 Ex) Gender -> (0,1)
# 범주형 변수 기울기 영향 X / Y절편 영향 O
# 범주형 범주가 n개이면 더비 변수 수 : n-1
# Ex) 혈액형 (A ,B ,AB ,O) - 3개 변수 필요
#   X1 X2 X3
# A 1  0  0
# B 0  1  0
# O 0  0  1
#AB 0  0  0 (base)

# Factor = 범주형 -> 더미 변수

# 의료비 예측
insurance = read.csv(file.choose())
str(insurance)
# $ age     : 나이 : int  19 18 28 33 32 31 46 37 37 60 ...
# $ sex     : 성별 :Factor w/ 2 levels "female","male": 1 2 2 2 2 1 1 1 2 1 ...
# $ bmi     : 비만도 지수 : num  27.9 33.8 33 22.7 28.9 ...
# $ children: 자녀 수 : int  0 1 3 0 0 0 1 3 2 0 ...
# $ smoker  : 흡연 유무 :Factor w/ 2 levels "no","yes": 2 1 1 1 1 1 1 1 1 1 ...
# $ region  : 지역 : Factor w/ 4 levels "northeast","northwest",..: 4 3 3 2 2 3 3 2 1 2 ...
# $ charges : 의료비(y) : num  16885 1726 4449 21984 3867

# 범주형 변수 : 성별(2) / 흡연 유무(2) / 거주지(4)
# base : level1(base) = 0 , level2 = 1

# 회귀 모델 생성
insurance2 = insurance[, -c(5:6)] # 흡연 유무 / 거주지 제외외
head(insurance2)

ins_model = lm(charges ~ ., data=insurance2)
# (Intercept) = -7460.0 , sexmale = 1321.7 

# femail = 0 , male = 1
# [해석] 여성에 비해서 남성의 의료비가 더 많이 증가가 되었다.
y_male = 1321.7 * 1 +( -7460.0)
y_female = 1321.7 * 0 + ( -7460.0)
y_male; y_female

x = c('male','female')
insurance2$sex = factor(insurance2$sex,levels=x)
insurance2
# male(base = 0)

ins_model = lm(charges ~ ., data=insurance2)
ins_model
# (Intercept) : -6138.2 / sexfemale : -1321.7
# [해석] 여성이 남성에 비해서 의료비 절감

male = subset(insurance2,sex=='male')
female = subset(insurance2,sex == 'female')
mean(male$charges)
mean(female$charges)

## dummy 변수 vs y 절편

insurance3 = insurance[-6]
head(insurance3)

ins_model2 = lm(charges~smoker , data =insurance3)
# (Intercept)    smokeryes  
#     8434        23616  


#base : smokerno = 0 /  smokeryes =1 
# [해석] 흡연자가 비흡연자에 비해서 23616 의료비 증가

no = subset(insurance3 , smoker == 'no')
mean(no$charges)

yes = subset(insurance3 , smoker == 'yes')
mean(yes$charges)

# 4개 범주 -> 3개 더미 변수
insurance4 = insurance
ins_model3 =lm(charges~region , insurance4)
# (Intercept)  regionnorthwest  regionsoutheast   regionsouthwest  
# 13406.4           -988.8           1329.0           -1059.4 
# northeast 

