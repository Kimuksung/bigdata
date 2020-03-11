# cat function을 사용하여 file save
# cat(data , file="C:\ITWILL\2_Rwork\R-script\sample.txt",append=T )

# text file read
# sample <- readLines("C:\ITWILL\2_Rwork\R-script\sample.txt")

# 차트 데이터 생성
chart_data <- c(305,700, 320, 460, 330, 480, 380, 520) 
names(chart_data) <- c("2016 1분기","2017 1분기","2016 2분기","2017 2분기","2016 3분기","2017 3분기","2016 4분기","2017 4분기")
str(chart_data)
chart_data

# 1. 이산변수 시각화 - 정수 단위 수(자녀, 판매...)
# 1) 막대차트 barplot main = 제목 col = 색깔 horiz = 가로 세로 beside
# par function -> chart를 여러개 띄어주는 역할
# 세로 막대 차트
max(chart_data)
barplot(chart_data,ylim = c(0,max(chart_data)+200), main="2016년 vs 2017 판매 현황" ,col=rainbow(8))#,horiz=F)

# 가로 막대 차트
barplot(chart_data,xlim = c(0,max(chart_data)+200), main="2016년 vs 2017 판매 현황" ,col=rainbow(8),horiz=T)#beside)

# 1행 2열 구조
par(mfrow=c(1,2))
VADeaths
str(VADeaths)
VADeaths["50-54",]

row_names<-row.names(VADeaths)
row_names
col_names<-colnames(VADeaths)
col_names
max(VADeaths)
barplot(VADeaths,beside=F,horiz=F,main="버지니아 사망 비율율",col=rainbow(length(row_names)))
barplot(VADeaths,beside=T,horiz=F,main="버지니아 사망 비율율",col=rainbow(length(row_names)))

par(mfrow=c(1,1))

#범례 추가
legend(x=4, y=200, legend = row_names, fill=rainbow(length(row_names)))

# 2) 점 차트
dotchart(chart_data, color=c("blue","red"), lcolor="black",
         pch=1:2, labels=names(chart_data), xlab="매출액",
         main="분기별 판매현황 점 차트 시각화", cex=1.2)

# 3) 파이 차트 (원 차트)
pie(chart_data, labels = names(chart_data),
    border='black', col=rainbow(length(names(chart_data))), cex=1.2)
  
title("2016~2017년도 분기별 매출현황")

str(iris)
table(iris$Species)
pie(table(iris$Species),col=rainbow(length(table(iris$Species))),main="iris flower")

# 연속 변수 시각화
# boxplot()
# 1) 상자 그래프 시각화 - 요약 통계
VADeaths
summary(VADeaths)
boxplot(VADeaths)

# 2) histogram visualization : 대칭성 확인
# hist()
data(iris) # iris 데이터 셋 가져오기
names(iris) #"child" "parent"
str(iris) # 928 2
head(iris)
summary(iris$Sepal.Length)
summary(iris$Sepal.Width)
par(mfrow=c(1,1))
hist(iris$Sepal.Width, xlab="iris$Sepal.Width",
     col="mistyrose", #색상
     main="iris 꽃받침 넓이 freq histogram", xlim=c(min(iris$Sepal.Width-1), max(iris$Sepal.Width+1)))

hist(iris$Sepal.Width, xlab="iris$Sepal.Width", #density -> 비율 형태로로
     col="mistyrose",freq = F,
     main="iris 꽃받침 넓이 density histogram", xlim=c(2.0, 4.5))

#밀도 분포 곡선
lines(density(iris$Sepal.Width), col="red")

# 3) 산점도 시각화
# plot(x,y)
x<-runif(15,min=1,max=100)
plot(x) #x= index , y= x
y<-runif(15,min=30, max=150)
plot(x,y) #= plot(y~x) 변하는 data 앞에다가

plot(iris$Sepal.Length,iris$Petal.Length,col=iris$Species)#, pch=5) 
par(mfrow=c(2,2)) # 2행 2열 차트 그리기
plot(iris$Sepal.Length,iris$Petal.Length,col=iris$Species, type="l") # 유형 : 실선
plot(iris$Sepal.Length,iris$Petal.Length,col=iris$Species, type="o") # 유형 : 원형과 실선(원형 통과)
plot(iris$Sepal.Length,iris$Petal.Length,col=iris$Species, type="h") # 직선
plot(iris$Sepal.Length,iris$Petal.Length,col=iris$Species, type="s") # 꺾은선

plot(price, type="o", pch=5) # 빈 사각형
plot(price, type="o", pch=15)# 채워진 마름모
plot(price, type="o", pch=20, col="blue") #color 지정
plot(price, type="o", pch=20, col="orange", cex=1.5) #character expension(확대)
plot(price, type="o", pch=20, col="green", cex=2.0, lwd=3) #lwd : line width

#만능차트
methods(plot) #어떤 type을 지원하여 주는지

# 시계열 자료
# plot.ts
WWWusage
par(mfrow=c(1,1)) 
plot(WWWusage)

#회 귀  모 델
# plot.lm
install.packages("UsingR")
library(UsingR)
library(help="UsingR")

data(Galton)
data(galton)
str(galton)# 회귀 용어 제안
model <- lm(child~ parent,data=galton)
plot(model)

#4) 산점도 행렬 : 변수 간의 비교
pairs(iris[-5])

# 꽃 종별 산정도 행렬
table(iris$Species)
pairs(iris[iris$Species=='setosa' , 1:4])
pairs(iris[iris$Species=='virginica' , 1:4])

# 5) 차트를 파일 저장
setwd("C:/ITWILL/2_Rwork/R-script") # 폴더 지정
jpeg("iris.jpg", width=720, height=480) # 픽셀 지정 가능
plot(iris$Sepal.Length, iris$Petal.Length, col=iris$Species)
title(main="iris 데이터 테이블 산포도 차트")
dev.off() # 장치 종료









































