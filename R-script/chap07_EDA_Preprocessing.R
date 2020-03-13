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
table(is.na(dataset))
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
for (i in 1:length(DF$grade)){  #모든 index 검색 grade 1과 4만 한거
  if(DF$grade[i] ==1 & is.na(DF$age[i])){ #index를 통해서 grade값과 age가 NA인지 구별
    grade1 = DF%>%filter(grade==1)
    temp=mean(grade1$age,na.rm=T) #평균 구하기
    DF$age[i]=temp
  }
  if(DF$grade[i] ==4 & is.na(DF$age[i])){
    grade4 = DF%>%filter(grade==4)
    temp=mean(grade4$age,na.rm=T)
    DF$age[i] = temp
  }
}
DF

# 3. 이상치(outlier) 발견과 정제
# - 정상 범주에서 크게 벗어난 값

# 1) 범주형(집단) 변수
gender = dataset$gender
gender #1 or 2 가 아닌 것들

# 이상치 발견 : table() , chart
table(gender)
pie(table(gender))

# 이상치 정제
dataset
library(dplyr)
temp = dataset %>% filter(gender ==1 | gender ==2 )
temp = subset(dataset,gender==1)
temp
pie(table(temp))
table(temp)
search()
pie

# price 2~10 정상 범주
dataset2 = subset(dataset,price>=2 & price <=10)
dim(dataset2)
plot(dataset2$price)
boxplot(dataset2$price)
str(dataset2)
head(dataset)

#dataset2 : age(20 ~69)
dataset2 = subset(dataset2 ,age >=20 &age<70)
plot(dataset2$age)
boxplot(dataset2$age)

# 3) 이상치 발견이 어려운 경우
boxplot(dataset$price)$stats # 이상치 내의 최소 , 최고 값들을 추출하여 이상치 내부에 있는것만 추출

temp = subset(dataset,price >= 2.1 & price <= 7.9)
boxplot(temp$price)

# 실습
library(ggplot2)
str(mpg)

# 정제 방법1 : 제거
hwy = mpg$hwy
length(hwy)
boxplot(hwy)$stats
mpg_df = mpg %>% filter(mpg$hwy>=boxplot(hwy)$stats[1] & mpg$hwy<=boxplot(hwy)$stats[5])
mpg_df <- subset(mpg,hwy>=12 & hwy<=37)
boxplot(mpg_df$hwy)
dim(mpg_df)

# 정제 방법2 : NA 처리
mpg
hwy_tmp = ifelse(mpg$hwy <12 | mpg$hwy > 37, NA ,mpg$hwy)
mpg$hwy2 = hwy_tmp
mpg_df = as.data.frame(mpg)
mpg_df[c('hwy','hwy2')]

# 4. 코딩 변경
# - 데이터 가독성, 척도 변경 , 최초 코딩 변경

# 1) 데이터 가독성 (1,2) -> 남,녀
# 형식) dataset$새칼럼[조건식] = "값"
dataset$gender2[dataset$gender == 1] <-"남자"
dataset$gender2[dataset$gender == 2] ="여자"
dataset

dataset2$resident2[dataset2$resident==1] = "1. 서울특별시"
dataset2$resident2[dataset2$resident==2] = "2. 인청광역시"
dataset2$resident2[dataset2$resident==3] = "3. 대전광역시"
dataset2$resident2[dataset2$resident==4] = "4. 대구광역시"
dataset2$resident2[dataset2$resident==5] = "5. 시구군"
dataset2

# 2) 척도 변경 : 연속형 -> 범주형
range(dataset2$age)
# 20~30 : 청년층 / 31~55 : 중년층 / 56 ~ : 장년층

dataset2$age2[dataset2$age <= 30 ] =  "청년층"
dataset2$age2[dataset2$age <= 55 & dataset2$age>30 ] =  "중년층"
dataset2$age2[dataset2$age > 55 ] =  "장년층"
dataset2

# 3) 역코딩 : 1-> 5, 5->1
table(dataset2$survey)

csurver = 6 - dataset2$survey
dataset2$survey2 = csurver 
dataset2

# 5. 탐색적 분석을 위한 시각화
# - 변수 간의 관계 분석

setwd("C:/ITWILL/2_Rwork/Part-II")
new_data = read.csv("new_data.csv")
new_data
str(new_data)
dim(new_data)

# 1) 범주형(명목/서열) vs 범주형(명목/서열)
# - 방법 : 교차테이블 , barplot

# 거주지역(5개) <-> 성별(2개)
tab1 = table(new_data$resident2 , new_data$gender2)
tab1
tab2 = table(new_data$gender2 , new_data$resident2 )
barplot(tab1,beside = T , horiz = T ,col =  rainbow(5),main= "성별에 따른 거주지역" , legend = row.names(tab1))
barplot(tab2,beside = T , horiz = T ,col =  rainbow(2),main= "지역에 따른 성별" , legend = row.names(tab2))

#정사각형 기준 
mosaicplot(tab1, col=rainbow(10) ,main=" 성별에 따른 percentage 그림")

# 고급 시각화 : 직업 유형
library(ggplot2) #chap08 자세히

# 미적 개체 생성
obj = ggplot(data = new_data , aes(x=job2,fill=age2))
# 막대 마트 추가
obj + geom_bar()

# 막대 마트 추가 : 밀도 1 기준 채우기
obj + geom_bar(position="fill")

table(new_data$job2,new_data$age2,useNA = "ifany")

# 2) 숫자형(비율) vs 범주형()
# 방법 : boxplot, 카테고리별 통계

install.packages("lattice")# 격자
library(lattice)
# 나이(연속형 -> 비율 ) <-> 직업 유형(명목)
densityplot(~age, groups = job2,data=new_data, auto.key = T)
# group = 집단 변수
# auto.key 범례 추가


# 3) 숫자형(비율) vs 범주형  vs 범주형
# (1) 구매 금액 => 성별과 직급으로 분류
densityplot(~price | factor(gender2), groups=position2 , data = new_data , auto.key = T)

#factor(집단 변수) : 범주의 수 만큼 격자 생성
# groups= 집단 변수 : 각 격자 내의 그룹 효과
# x축 , group = y축 , factor 몇개의 그래프

densityplot(~price | factor(position2), groups=gender2 , data = new_data , auto.key = T)

# 4) 숫자형 vs 숫자형 / 숫자형 vs 숫자형 vs 범주형
# - 방법 : 상관 계수 , 산점도 , 산점도 행렬

# (1) 숫자형 vs 숫자형
cor(new_data$age,new_data$price) #NA 
new_data1 = na.omit(new_data)
cor(new_data1$age,new_data1$price) # +-0.3~0.4이상이어야 상관관계가 있다.
# 나이와 price는 상관관계 X

plot(new_data1$age,new_data1$price)

# (2) 숫자형 vs 숫자형 vs 범주형
xyplot(price ~ age |factor(gender2) , data=new_data)

# 6. 파생 변수 생성
# 기존 변수를 이용하여 새로운 변수 생성
# 1) 사칙연산
# 2) 1:1 -> 기존 칼럼 -> 새로운 칼럼(1)
# 3) 1:n -> 기준 변수 -> 새로운 칼럼(n)

#고객 정보 테이블
user_data = read.csv("user_data.csv")
str(user_data)

# 1:1 -> 기존 칼럼 -> 새로운 칼럼(1)
# 더미 변수 : 1,2 -> 1 3,4 ->2
user_data$house_type2 = ifelse(user_data$house_type==1 | user_data$house_type==2 ,1 , 2)
table(user_data$house_type2)

# 1:n -> 기준 변수 -> 새로운 칼럼(n)

# 지불 정보 테이블
pay_data = read.csv('pay_data.csv')
str(pay_data)
#$ user_id     : int  1001 1002 1003 1003 1003 1003 1007 1007 1007 1007 ...
#$ product_type: int  1 2 3 4 5 1 2 3 4 5 ...
#$ pay_method  : Factor w/ 4 levels "1.현금","2.직불카드",..: 1 2 3 3 3 3 2 2 2 2 ...
#$ price


library(reshape2)
#dcast(dataset, 행 집단 변수 ~ 열 집단 변수, function)

#고객별 product_type에 따른 price 합계
product_price = dcast(pay_data,user_id~product_type,sum)
dim(product_price) #303  400명 중 303명만 구입햇다.
names(product_price) = c("user_id", "식료품(1)","생필품(2)","의류(3)","잡화(4)","기타(5)")
str(product_price)

# 파생 변수 추가(join)
library(dplyr)
# 형식) left_join(df1,df2,by='column')
user_pay_data = left_join(user_data , product_price, by="user_id")
dim(user_pay_data)
head(user_pay_data)
str(user_pay_data)

user_pay_data2 = user_pay_data
user_pay_data2[is.na(user_pay_data2)] = 0
head(user_pay_data2)

# 사칙 연산 : 총 구매 금액
names(user_pay_data)

user_pay_data$tot_price = rowSums(user_pay_data[7:11])
head(user_pay_data)






















