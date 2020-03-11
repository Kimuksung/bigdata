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









































