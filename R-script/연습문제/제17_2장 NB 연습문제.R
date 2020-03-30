##########################
## 제2-2장 NB 연습문제 
##########################

# 문) Spam 메시지 데이터 셋을 이용하여 NB 분류모델을 생성하고,
# 분류정확도와 F 측정치를 구하시오. 

# 실습 데이터 가져오기(TM에서 전처리한 데이터)
setwd("C:/ITWILL/2_Rwork/Part-IV")
sms_data <- read.csv('sms_spam_tm.csv')
dim(sms_data) # [1] 5558(row) 6824(word) - 6157
str(sms_data)

# X 칼럼 제외 
sms_data.df <- sms_data[-1] # 행번호 제외 
head(sms_data.df)
str(sms_data.df) # 5558 obs. of  6823 variables:
sms_data.df$sms_type
dim(sms_data.df)
# 1. train과 test 데이터 셋 생성 (7:3)
idx <- sample(1:nrow(sms_data.df), 0.7*nrow(sms_data.df))
train <- sms_data.df[idx, ]
test <- sms_data.df[-idx, ]

# 2. model 생성 - train_sms
model <- naiveBayes(train[-1], train$sms_type)
model = naiveBayes(sms_type ~ ., data = train)
# 3. 예측치 생성 - test_sms
p <- predict(model, test)
tab = table(p, test$sms_type)
tab

# 4. 정분류율(Accuracy)
acc = (tab[1,1]+tab[2,2]) / nrow(test) #0.9766187

# 5. F measure(f1 score)
precision <- sum(predict & true) / retrieved
precision = tab[2,2] / sum(tab[,2]) #0.9009009
recall <- sum(predict & true) / sum(true)
recall = tab[2,2] / sum(tab[2,]) #0.921659
Fmeasure <- 2 * precision * recall / (precision + recall) # 0.9111617

#-------------------------------------
sms_data <- read.csv('sms_dtm_df.csv')
dim(sms_data) # [1] 5558(row) 6824(word) - 6157
str(sms_data)

# X 칼럼 제외 
# 1. train과 test 데이터 셋 생성 (7:3)
idx <- sample(1:nrow(sms_data), 0.7*nrow(sms_data))
train <- sms_data[idx, ]
dim(train)
test <- sms_data[-idx, ]
# 2. model 생성 - train_sms
model <- naiveBayes(train[-1], train$sms_data.type)
model = naiveBayes(sms_data.type ~ ., data = train)
# 3. 예측치 생성 - test_sms
p <- predict(model, test)
tab = table(p, test$sms_type)
tab

# 4. 정분류율(Accuracy)
acc = (tab[1,1]+tab[2,2]) / nrow(test) #0.9766187

# 5. F measure(f1 score)
precision <- sum(predict & true) / retrieved
precision = tab[2,2] / sum(tab[,2]) #0.9009009
recall <- sum(predict & true) / sum(true)
recall = tab[2,2] / sum(tab[2,]) #0.921659
Fmeasure <- 2 * precision * recall / (precision + recall) # 0.9111617

