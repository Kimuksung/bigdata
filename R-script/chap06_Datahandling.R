#Data Handling

# 1. dplyr 패키지 
install.packages("dplyr")
library(dplyr)

# 1) 파이프 연산자 : %>%
# 형식) df%>%function1()%>%function2()

iris %>% head() %>% filter(Sepal.Length>=5.0)

install.packages("hflights")
library(hflights)

str(hflights)

# 2) tbl_df() : 콘솔 크기 만큼 자료를 나타내준다.
hflights_df <- tbl_df(hflights)
hflights_df

# 3) filter() : 행 추출
# 형식) df%>% filter( 조건식)
names(iris)
iris%>% filter(Species=="setosa") %>% head
iris_df<-iris%>% filter(Sepal.Width >3) %>% head
iris_df
str(iris_df)

hflights_df %>% filter(Month==1 & DayofMonth==1)

# 4) arrange() : 정렬 함수
# 형식) df %>% arrange( column명)  default -> 오름차순
iris %>% arrange(Sepal.Width) %>% head()
iris %>% arrange(desc(Sepal.Width)) %>% head() # 내림차순

arrange(hflights_df, Year , desc(Month),ArrTime)

# 5) select() : 열 추출
# 형식) df %>% select()
iris %>% select(Sepal.Length,Petal.Length,Species)%>%head()

select(hflights_df,ArrTime,DepTime,TailNum)
select(hflights_df,Year:DayOfWeek)

# Month 기준으로 내림차순 정렬 뒤, Year , Month , AirTime

hflights_df%>% arrange(desc(Month))%>% select(Year,Month,ArrTime)

# 6) mutate() : 파생 변수 생성
# 형식_ df %>% mutate(변수 = 함수)

iris %>% mutate(diff = Sepal.Length-Sepal.Width) %>% arrange(desc(diff)) %>% head()

mutate(hflights_df, diff_deplay = ArrDelay - DepDelay) %>%  select(diff_deplay)

#7) summarise() : 요약통계 함수
# 형식) df %>% summarise(변수 = 통계함수(0))

iris %>% summarise(col1_avg = mean(Sepal.Length), col2_sd = sd(Sepal.Length)) 

summarise(hflights_df,delay = mean(DepDelay,na.rm = T),delay_tot= sum(DepDelay,na.rm=T))

# 8) group_by(dataset, 집단 변수) : 
# 형식) df %>% group_by(집단 변수)
names(iris)

table(iris$Species)

grp =iris %>% group_by(Species)
table(iris %>% group_by(Species=="setosa"))

summarise(grp,mean(Sepal.Length))
summarise(grp,sd(Sepal.Length))

install.packages("ggplot2")
library(ggplot2)

data("mtcars") # 자 동 차 연 비
head(mtcars)
str(mtcars)
table(mtcars$cyl)


grp = group_by(mtcars,cyl)
grp
#각 cyl 별 연비 평균 표준편차
summarise(grp, mpg_avg=mean(mpg) , mpg_sd = sd(mpg))

grp2 = group_by(mtcars,gear)
summarise(grp2,wt_sd= sd(wt),wt_mean= mean(wt))

# 2개의 집단 변수 -> 그룹화
grp3 = group_by(mtcars,cyl,gear)
summarise(grp3 , mpg_avg = mean(mpg), mpg_sd = sd(mpg))

#group_by(dataset,집단 변수)
#각 항공기별 비행 편수가 40% 이상이고 평균 비행거리가 2,000 마일 이상인 경우 평균 도착 지연 시간을 ㅗ학인

temp=hflights_df%>%group_by(TailNum)
planes_state = summarise(temp,count= n(),dist_avg = mean(Distance,na.rm=T),
                         delay_avg=mean(ArrDelay,na.rm=T)) #비행 편수 , 평균 비행거리 , 
planes_state

#3) 항공기별 요약 통계 필터링
planes_state%>% filter(count>=40 & dist_avg>=2000)

# 2.reshape2
# 연관 분석시에 주로 사용한다.

install.packages('reshape2')
library(reshape2)

#1) dcast() : long -> wide
data  = read.csv(file.choose())
head(data)

# Date / ID / 수량
names(data)
# 형식) dcast(datset,row ~ col , func )
data
wide = dcast(data,Customer_ID~Date,sum) 
wide

library(ggplot2)
data("mpg")
str(mpg)
mpg
mpg_df <- as.data.frame(mpg)
mpg_df
str(mpg_df)
library(dplyr)
mpg_df <- select(mpg_df,c(cyl,drv,hwy))
mpg_df
head(mpg_df)
# 교차셀에 hwy 합계
hwy_sum = dcast(mpg_df,cyl~drv,sum)

# 교차셀에 hwy 출현 건수
hwy_len = dcast(mpg_df,cyl~drv,length)

# 교차 분할표
table(행집단변수, 열집단변수)
table(mpg_df$cyl,mpg_df$drv)
unique(mpg_df$cyl)
unique(mpg_df$drv)

# 2) melt() : wide -> long
long = melt(wide,id="Customer_ID")
long
wide
# Customer_ID : 기준 column
# vairable : 열이름
# value : 교차셀의 값

data
names(long) <- c("Customer_ID", "Date","Buy")

#wide -> long
data("smiths")
smiths
long2 = melt(smiths,id="subject")
long2
long3 = melt(smiths,id=1:2)
long3

#long -> wide
wide2 = dcast(long2,subject~ ...) # 나머지 컬럼

# 3. acast(dataset, 행 ~ 열 ~면)
data("airquality")
str(airquality)

table(airquality$Month)
table(airquality$Day)

# wide -> long
air_melt = melt(airquality, id = c("Month","Day"),na.rm = T)
air_melt
str(air_melt)
#[일 ,월, variable] => [행 ,열 ,면]
#acast(dataset,Day~Month-Wariable)

air_arr3d = acast(air_melt,Day~Month~variable) 
dim(air_arr3d)

# 오존 data
air_arr3d[,,1]

# 태양열 data
air_arr3d[,,2]

####################
#추가 내용
####################

# 4. URL 만들기 : http://www.naver.com
# 1) base url 만들기
baseUrl = "http://www.sbus.or.kr/2018/lost/lost_02.htm"

# 2) page query 만들기
no <- 1:5
library(stringr)
page <- str_c('?Page=',no)
page

# outer(x(1),Y(n),function)
temp = outer(baseUrl,page,str_c)
# 2d -> 1d
page_url = sort(as.vector(temp))
page_url

# 3) 특정 유형 쿼리 추가 &sear=2
no = 1:3
sear= str_c("&sear=",no)
sear
final_url = outer(page_url,sear,str_c)
final_url = as.vector(final_url)
final_url






















