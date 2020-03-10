# 1. data 불러오기 (키보드 입력 및 파일 가져오기)
# 1) 키보드 입력

x<-scan() #숫자 입력

# 문자입력
string <- scan(what = character())

# 파일 읽기
setwd("C:/ITWILL/2_Rwork/Part-I")

# 1) txt file 가져오기
student<-read.table("student.txt")
student
str(student)
#기본 제목이 v1....vn으로 만들어진다.

#기본 제목이 있는경우
student2<-read.table("student2.txt", header=TRUE ,sep=";")
student2
str(student2)

# 결측지 처리하기
student3<-read.table("student3.txt", header=TRUE, na.strings=c("-","&") )
student3
student3$'키'

mean(student3$'키',na.rm=T)
str(student3)

# read.csv
student4<-read.csv("student4.txt",na.strings="-")
student4

#탐색기 이용 파일 선택
read.csv(file.choose())

# xls/xlsx package install 필요
install.packages("xlsx")
library(xlsx)


kospi <- read.xlsx("sam_kospi.xlsx",sheetIndex = 1)
kospi

# 한글이 포함된 xlsx 파일 읽기

st_excel <- read.xlsx("studentexcel.xlsx",sheetIndex = 1,encoding = 'UTF-8')

# 인터넷 파일 읽기
# 데이터 셋 제공 사이트 
# http://www.public.iastate.edu/~hofmann/data_in_r_sortable.html - Datasets in R packages
# https://vincentarelbundock.github.io/Rdatasets/datasets.html
# https://r-dir.com/reference/datasets.html - Dataset site
# http://www.rdatamining.com/resources/data

titanic <- read.csv("https://vincentarelbundock.github.io/Rdatasets/csv/COUNT/titanic.csv")
str(titanic)
dim(titanic)
head(titanic )

#생존여부
table(titanic$survived)

table(titanic$sex)
tab <-table(titanic$survived,titanic$sex)

options(max.print=999999999)

barplot(tab,col=rainbow(2))


# 2. data 저장하기
# 1) 화면 출력
z=50
cat('z=',z)

# 2) 파일 저장
# write.table : 구분자 공백 / 특수문자
# write.csv : 구분자 콤마
# write.xlsx :엑셀 패키지 필수

setwd("C:/ITWILL/2_Rwork/output")
titanic
write.table(titanic,"titanic.txt",row.names=FALSE)
write.table(titanic,"titanic2.txt",row.names=FALSE,quote=FALSE)


titanic_df<- titanic[-1]
head(titanic_df)
write.csv(titanic_df,"titanic_df.csv",row.names = F,quote=F)

search()
write.xlsx(titanic,"titanic.xlsx",sheetName = "titanic", row.names=FALSE)

name <- c("kim","lee","choi","park")
which(name=="choi") 

library(MASS)
data("Boston")
str(Boston)
names<- names(Boston)
names

#x(독립변수), y(종속 변수) 선택
#n개의 column의 data들이 있는데 이를 하나의 data에 가장 크게 영향을 끼치는 것을 찾는다.
# y = 하나의 data
y_col <- which(names=="medv")

Y <- Boston[y_col] # y(종속 변수)
X <- Boston[-y_col] # x(독립변수)

# iris을 dataset을 대상으로 x변수(1~4)
data("iris")
names<-names(iris)
names(iris)
names
y_col <- which(names=="Species" )

Y <- iris[y_col]
Y
X <- iris[-y_col]

#for 문
# 열거형 객체
num <- scan()
for(i in 1:5){
  if(num[i]%%2==0){
    print(num[i])
  }
}

setwd("C:/ITWILL/2_Rwork/Part-I")
sample <-read.csv("sam_kospi.csv")
str(sample)

#칼럼 추가 high- low
sample$diff <- sample$High - sample$Low
str(sample)

diff_result=""
row <- nrow(sample) #칼럼 갯수
for( i in 1:nrow(sample)){
  if(sample$diff[i]>=mean(sample$diff)){
    diff_result[i]= "평균 이상"
  }else{
    diff_result[i]= "평균 이하"
  }
}
sample$diff_reulst <- diff_result
head(sample)


#bug report
install.packages('RSADBE')
library(RSADBE)
data("Bug_Metrics_Software")
str(Bug_Metrics_Software)

#발표 전
Bug_Metrics_Software[,,1]

rowSums(Bug_Metrics_Software[,,1]) # software별 bug 합계
colSums(Bug_Metrics_Software[,,1]) # bug 별 bug 합계
rowMeans(Bug_Metrics_Software[,,1]) #software 별 평균
colMeans(Bug_Metrics_Software[,,1]) #bug 별 평균

#발표 후
Bug_Metrics_Software[,,2]

Bug_Metrics_Software

# 난수 생성과 확률 분포
# 1) 정규 분포를 따르는 난수 - 연속 확률 분포(실수형)
# 형식) rnorm(n,mean=(),sd=1)
n<-1000
r<-rnorm(n)
hist(r)

# 2) 균등분포를 따르는 난수 - 연속 확률 분포(실수형)
# 형식) runif(n,min=,max=)
r2<-runif(n,min=10,max=100)
r2
hist(r2)

# 3) 이항 분포를 따르는 난수 - 이산확률 분포(정수형)
# 형식) rbinom(n,size=,확률)
set.seed(123) #똑같은 data를 가질 수 있도록 해준다.(매번 바뀌는거 금지)
r3<-rbinom(n,1,0.5)
r3
hist(r3)
table(r3)

# 4) sample
sample(10:20,5)
sample(c(10:20,50:100),10)

#train / test set 생성 시 사용 70% / 30% hold-out 방식 
dim(iris)
idx<-sample(nrow(iris), size=nrow(iris)*0.7)
range(idx) 150
length(idx) 105
train<- iris[idx,]
test<- iris[-idx,]
dim(train) #105개 70%
dim(test) #45개 30%

# 4. 행렬 연산 내장 함수
x<- matrix(1:9,nrow=3,byrow=T)
x
y<- matrix(1:3,nrow=3)
y

x%*%y
