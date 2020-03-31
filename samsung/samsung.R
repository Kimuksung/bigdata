setwd("C:\\ITWILL\\2_Rwork\\samsung")

library(stringr)

df1 = read.csv('mealData_customer_train.csv', stringsAsFactors = FALSE)
df2 = read.csv('mealData_meal_train2.csv', stringsAsFactors = FALSE)
df3 = read.csv('weather2.csv', stringsAsFactors = FALSE)
temp = c('2018/01/01','[\'평균기온::-1\']','[]') # 빠진 부분에 대해서 하나 추가

df3 = rbind(temp,df3) 
names(df3) = c('SELL_DATE', 'temper', 'rain') #dataframe naming 
df3$SELL_DATE 
df3$SELL_DATE= str_replace_all(df3$SELL_DATE, "/", "-")  #date 똑같은 형태로 변환 join하기 위해

df4<-merge(x=df1,y=df2,by="CUSTOMER_ID") # dataframe join
df<-merge(x=df4,y=df3,by="SELL_DATE")

head(df,100)
df$temper= str_replace_all(df$temper, "\\[\\'평균기온:", "") #data 전처리
df$temper= str_replace_all(df$temper, "\\'\\]", "")
df$rain= str_replace_all(df$rain, "\\[\\'일강수량:", "")
df$rain= str_replace_all(df$rain, "\\'\\]", "")
df$rain= str_replace_all(df$rain, "\\[\\]", "0")

str(df)
df$GENDER = as.factor(df$GENDER)
df$MENU = as.factor(df$MENU)
df$BRAND = as.factor(df$BRAND)
df$temper = as.numeric(df$temper)
df$rain = as.numeric(df$rain)
df$BIRTH_YEAR= 2021 - df$BIRTH_YEAR

table(df$temper)
table(df$SELL_DATE)

#온도 category화
df$temper2[df$temper<=-10]="1.~-10" 
df$temper2[df$temper>-10 & df$temper <=-5]="2.-9~-5"
df$temper2[df$temper>-5 & df$temper <=0]="3.-4~0"
df$temper2[df$temper>0 & df$temper <=5]="4.1~5"
df$temper2[df$temper>5 & df$temper <=10]="5.6~10"
df$temper2[df$temper>10 & df$temper <=15]="6.11~15"
df$temper2[df$temper>15 & df$temper <=20]="7.16~20"
df$temper2[df$temper>20 & df$temper <=25 ]="8.21~25"
df$temper2[df$temper>25 & df$temper <=30 ]="9.26~30"
df$temper2[df$temper>30 ]="9.31~"
head(df)

table(df$temper2)

#--------------------------------------------------
library(dplyr)
library(tidyr)
library(ggplot2)
#temp <- df %>% group_by(temper2, BRAND) %>%  tally() 행 갯수로 세는거
# sum으로 세기 전체 총합
temp <- df %>% group_by(temper2)  

brand_sum = aggregate(temp$QUANTITY, by=list(temp$temper2), FUN=sum)
names(brand_sum) = c('temper','sum')
ggplot(brand_sum, aes(temper, sum ))+geom_bar(stat="identity", position="dodge")



# brand별 총합
str(df)
a = table(df$temper2)

temper_brand_sum=df %>%group_by(temper2, BRAND) %>% summarise(a_sum=sum(QUANTITY) )
temper_brand_sum$temp[temper_brand_sum$temper2=='1.~-10']=a[1]
temper_brand_sum$temp[temper_brand_sum$temper2=='2.-9~-5']=a[2]
temper_brand_sum$temp[temper_brand_sum$temper2=='3.-4~0']=a[3]
temper_brand_sum$temp[temper_brand_sum$temper2=='4.1~5']=a[4]
temper_brand_sum$temp[temper_brand_sum$temper2=='5.6~10']=a[5]
temper_brand_sum$temp[temper_brand_sum$temper2=='6.11~15']=a[6]
temper_brand_sum$temp[temper_brand_sum$temper2=='7.16~20']=a[7]
temper_brand_sum$temp[temper_brand_sum$temper2=='8.21~25']=a[8]
temper_brand_sum$temp[temper_brand_sum$temper2=='9.26~30']=a[9]
temper_brand_sum$temp[temper_brand_sum$temper2=='9.31~']=a[10]

ggplot(temper_brand_sum, aes(BRAND, a_sum ),fill=temper2)+geom_bar(stat="identity", position="dodge")
qplot(temper2, a_sum, data=temper_brand_sum, color=factor(BRAND), geom="bar")
ggplot(temper_brand_sum, aes(temper2 , a_sum / temp , color=BRAND),fill = BRAND)+geom_bar(stat="identity", position="dodge")

#ggplot(temp, aes(temper2, n , fill = BRAND))+geom_bar(stat="identity", position="dodge")
ggplot(brand_sum, aes(BRAND, sum ))+geom_bar(stat="identity", position="dodge")

table(df$BRAND)
temp2 = subset(df,BRAND=='탕맛기픈')  
temp2 <- temp2 %>% group_by(temper2) %>%  tally()

ggplot(temp2, aes(temper2, n ))+geom_bar(stat="identity", position="dodge")




str(df)
#plot(df$temper, df$QUANTITY, col=df$BRAND)
#temper_brand_sum=df %>%group_by(temper, BRAND) %>% summarise(a_sum=sum(QUANTITY))
subset(df,BRAND=='KOREAN1')
temper_brand_sum=subset(df,BRAND=='KOREAN1') %>%group_by(temper) %>% summarise(a_sum=sum(QUANTITY))
#plot(temper_brand_sum$temper, temper_brand_sum$a_sum, col=temper_brand_sum$BRAND)
plot(temper_brand_sum$temper, temper_brand_sum$a_sum)

library (dplyr)
ggplot(temper_brand_sum, aes(x = temper, y = a_sum)) + geom_bar (stat="identity")
library(lattice)
histogram(temper_brand_sum$temper, temper_brand_sum$a_sum)

#------------------
#사원별 구매 횟수
library (dplyr)
length(setdiff (df1$CUSTOMER_ID, df$CUSTOMER_ID)) #230명은 사원이지만 한번도 안먹엇다
length(unique(df$CUSTOMER_ID)) # 10570
people_eat = df %>% group_by(CUSTOMER_ID) %>% summarise(sum(QUANTITY))
names(people_eat) = c('CUSTOMER_ID', 'QUANTITY')
arrange(people_eat, desc(QUANTITY)) #정렬
mean(people_eat$QUANTITY) #97.57379
t = table(people_eat$QUANTITY>=100) #평균 보다 높게 잡았다.
people_eat$CUSTOMER_ID[people_eat$QUANTITY>=100]

df$samsung = df$CUSTOMER_ID %in% people_eat$CUSTOMER_ID[people_eat$QUANTITY>=100]
head(df)

samsung = subset(df,samsung==TRUE) # 단골
not_samsung = subset(df,samsung==FALSE) # 신규

#--------------------
str(df)
dim(df)
unique(df$rain)
table(df$rain==0)
# FALSE   TRUE 
# 267297 756176

#round (pi, digits = 40)
head(rain_brand_sum,20)
rain_brand_sum=df %>%group_by(rain) %>% summarise(a_sum=sum(QUANTITY) )
# 762062
sum(rain_brand_sum$a_sum)
#1031355
# 비가 온날의 판매량  1031355 - 762062 = 269293
length(unique(df$SELL_DATE[df$rain==0]))#306
length(unique(df$SELL_DATE[df$rain!=0]))#104

# 비가 온날의 판매량 / 비가 왔던 날 갯수
# 269293 / 104 = 2589.3557692307691
# 비가 오지 않는 날의 판매량 / 비가 오지 않는 날 갯수
# 762062 / 306 = 2490.3986928104573
x = 2589.3557692307691
y = 2490.3986928104573
library(lattice)
barplot(c(x,y),names())

KOREAN = subset(df , BRAND=='KOREAN1')
head(KOREAN)
korean1_rain_sum=KOREAN %>%group_by( rain) %>% summarise(a_sum=sum(QUANTITY) )
length(unique(df$SELL_DATE[df$rain==0&df$BRAND=='KOREAN1']))
length(unique(df$SELL_DATE[df$rain!=0&df$BRAND=='KOREAN1']))
# 비가 오지 않는 날의 판매량 = 102550
# 비가 오지 않는 날 = 254
# 102550 / 254 = 403.74015748031496
sum(korean1_rain_sum$a_sum)
# 비가 온날의 판매량 138622 - 102550 = 36072
# 비가 온날 = 88
# 36072 / 88 = 409


TakeOut = subset(df , BRAND=='TakeOut')
head(TakeOut)
takeout_rain_sum=TakeOut %>%group_by( rain) %>% summarise(a_sum=sum(QUANTITY) )
length(unique(df$SELL_DATE[df$rain==0&df$BRAND=='TakeOut']))
length(unique(df$SELL_DATE[df$rain!=0&df$BRAND=='TakeOut']))
# 비가 오지 않는 날의 판매량 = 121140
# 비가 오지 않는 날 = 254
# 121140 / 254 = 476.92913385826773
sum(takeout_rain_sum$a_sum)
# 비가 온날의 판매량 163706 - 121140 = 42566
# 비가 온날 = 88
# 42566 / 88 = 483.70454545454544


#----------------------
#     CUSTOMER_ID QUANTITY
# 1     2061390      791
# 2     2147028      717
# 3     2136400      608
# 4     2044358      579
# 5     2256444      575
# 6     2677386      568
# 7     2272739      544
# 8     2718042      540
# 9     2577611      527
# 10     2526086      514

#단골(100번 이상 먹은 사람들)의 개인별 브랜드 선호도(max value)
people_eat = samsung %>% group_by(CUSTOMER_ID) %>% summarise(sum(QUANTITY)) 
names(people_eat) = c('CUSTOMER_ID', 'QUANTITY')
custom_data = arrange(people_eat, desc(QUANTITY))$CUSTOMER_ID[1:4191 ]
dim(people_eat) #4191 

for(i in 1:length(custom_data)){
#for(i in 1:10){
  custom1 = subset(samsung, CUSTOMER_ID==custom_data[i])
  t = table(custom1$BRAND)
  best=names(t)[t == max(t)]
  print(best)
  samsung$brand_prefer[samsung$CUSTOMER_ID==custom_data[i]]=best
} 
table(samsung$brand_prefer)
# Chef`sCounter       KOREAN1       KOREAN2       TakeOut       Western 
# 32321        193751        122749        275152         11373 
# 가츠엔  고슬고슬비빈    나폴리폴리      스냅스낵    싱푸차이나 
# 33745         33218         35774          6388         66637 
# 아시안픽스    우리미각면      탕맛기픈 
# 6199         36216         37376 
summary(samsung)
prop.table(table(samsung$brand_prefer))*100
# Chef`sCounter              KOREAN1              KOREAN2              TakeOut 
# 3.62790843855476330 21.74780755169777891 13.77810503772032646 30.88475798042202314 
# Western               가츠엔         고슬고슬비빈           나폴리폴리 
# 1.27657568366335572  3.78774698366481521  3.72859325243377748  4.01549446121277498 
# 스냅스낵           싱푸차이나           아시안픽스           우리미각면 
# 0.71702852960885577  7.47974798490064519  0.69581400360759194  4.06510726805170997 
# 탕맛기픈 
# 4.19531282446158293 

#비단골 개인별 브랜드 선호도
#단골(100번 이상 먹은 사람들)의 개인별 브랜드 선호도(max value)
people_eat = not_samsung %>% group_by(CUSTOMER_ID) %>% summarise(sum(QUANTITY)) 
names(people_eat) = c('CUSTOMER_ID', 'QUANTITY')
custom_data = arrange(people_eat, desc(QUANTITY))$CUSTOMER_ID[1:6379 ]
dim(people_eat)#6379

for(i in 1:length(custom_data)){
  custom1 = subset(not_samsung, CUSTOMER_ID==custom_data[i])
  t = table(custom1$BRAND)
  best=names(t)[t == max(t)]
  print(best)
  not_samsung$brand_prefer[not_samsung$CUSTOMER_ID==custom_data[i]]=best
} 
table(not_samsung$brand_prefer)
# Chef`sCounter       KOREAN1       KOREAN2       TakeOut       Western 
# 4214         22707         19117         25789          4590 
# 가츠엔  고슬고슬비빈    나폴리폴리      스냅스낵    싱푸차이나 
# 12833          4612          6541          2872         11224 
# 아시안픽스    우리미각면      탕맛기픈 
# 2928          6158          8989 
summary(not_samsung)
prop.table(table(not_samsung$brand_prefer))*100
# Chef`sCounter             KOREAN1             KOREAN2 
# 3.1786021391826451 17.1277927798814247 14.4198711662920331 
# TakeOut             Western              가츠엔 
# 19.4525321707122067  3.4622173276811443  9.6798768989394599 
# 고슬고슬비빈          나폴리폴리            스냅스낵 
# 3.4788118333911626  4.9338482658741540  2.1663372908715131 
# 싱푸차이나          아시안픽스          우리미각면 
# 8.4662150949658308  2.2085778508606513  4.6449530073770120 
# 탕맛기픈 
# 6.7803641739707636 

# 위 값을 이용하여 일반적인 갯수를 맞추어보자.
# samsung data에서 2018/1/1에 TAKE OUT한사람 실제 data와 예측 data

