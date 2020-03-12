# 1. 탐색적 데이터 조회

# 실습 데이터 읽어오기
setwd("C:/ITWILL/2_Rwork/Part-II")
dataset <- read.csv("dataset.csv", header=TRUE) # 헤더가 있는 경우
# dataset.csv - 칼럼과 척도 관계 


# 1) 데이터 조회
# - 탐색적 데이터 분석을 위한 데이터 조회 
dataset
# (1) 데이터 셋 구조
names(dataset) # 변수명(컬럼)
attributes(dataset) # names(), class, row.names
str(dataset) # 데이터 구조보기
dim(dataset) # 차원보기 : 300 7
nrow(dataset) # 관측치 수 : 300
length(dataset) # 칼럼수 : 7 
length(dataset$resident) # 300

# (2) 데이터 셋 조회
# 전체 데이터 보기
dataset # print(dataset) 
View(dataset) # 뷰어창 출력

# 칼럼명 포함 간단 보기 
head(dataset)
head(dataset, 10) 
tail(dataset) 

# (3) 칼럼 조회 
# 형식) dataframe$칼럼명   
dataset$resident
length(dataset$age) # data 수-300개 

# 형식) dataframe["칼럼명"] 
dataset["gender"] 
dataset["price"]

# $ vs index
temp1 <- dataset$resident #$ -> int[1:300] vector
temp2 <- dataset['resident'] #index -> data.frame
str(temp1);str(temp2)


# 형식) dataframe[색인] : 색인(index)으로 원소 위치 지정 
dataset[2] # 두번째 컬럼
dataset[6] # 여섯번째 컬럼
dataset[3,] # 3번째 관찰치(행) 전체 -> vector
dataset[,3] # 3번째 변수(열) 전체

# dataset에서 2개 이상 칼럼 조회
dataset[c("job", "price")]
dataset[c("job":"price")] # error 
dataset[c(2,6)] 

dataset[c(1,2,3)] 
dataset[c(1:3)] 
dataset[c(2,4:6,3,1)] 
dataset[-c(2)] # dataset[c(1,3:7)] 

# 2. 결측치(NA) 발견과 처리
# 9999999 - NA

# 결측치 확인
summary(dataset$price)
table(is.na(dataset$price))
table(is.na(dataset)) #all data na confirm

# 1) 결측치 제거
price2 = na.omit(dataset$price) #vector
price2

dataset2 <- na.omit(dataset)
dataset2
dim(dataset) #[1] 300   7
dim(dataset2) #[1] 209   7

#특정 칼럼 기준 결측치 제거 -> subset 생성
stock = read.csv(file.choose())
str(stock)

# Market.Cap 기준 (시가총액)
library(dplyr)
stock$Market.Cap
stock_df = stock %>% filter(!is.na(Market.Cap))
dim(stock_df) #[1] 5028   69
subset(stock,!is.na(Market.Cap))
dim(subset(stock,!is.na(Market.Cap))) #[1] 5028   69

# 2) 결측치 처리(0)
x<- dataset$price
dataset$price2 = ifelse(is.na(x),0,x)
head(dataset)

# 3) 결측치 처리(평균으로 대체)
dataset$price3 = ifelse(is.na(x),mean(x,na.rm = T),x)


head(dataset[c('price','price2','price3')])

#통계적 방법의 결측치 처리
# ex) 1~4: age 결측치 -> 각 학년별 평균으로 대체

age <- round(runif(n=12 , min = 20, max =25 ))
age
grade = rep(1:4,3)
grade

age[5] = NA
age[8] = NA

DF = data.frame(age,grade)
DF

grade1 = DF%>%filter(grade==1)
grade1
mean(grade1)
grade1 = ifelse(is.na(grade1$age),mean(grade1$age,na.rm=T),grade1$age)
grade1


# 각각 평균
for (i in 1:length(DF$grade)){
  if(DF$grade[i] ==1 & is.na(DF$age[i])){
    grade1 = DF%>%filter(grade==1)
    temp=mean(grade1$age,na.rm=T)
    DF$age[i]=temp
  }
  if(DF$grade[i] ==4 & is.na(DF$age[i])){
    grade4 = DF%>%filter(grade==4)
    temp=mean(grade4$age,na.rm=T)
    DF$age[i] = temp
  }
}
DF













