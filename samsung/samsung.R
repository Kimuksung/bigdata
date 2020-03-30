setwd("C:\\ITWILL\\2_Rwork\\samsung")

library(stringr)

df1 = read.csv('mealData_customer_train.csv', stringsAsFactors = FALSE)
df2 = read.csv('mealData_meal_train2.csv', stringsAsFactors = FALSE)
df3 = read.csv('weather2.csv', stringsAsFactors = FALSE)
temp = c('2018/1/1','[\'평균기온::-1\']','[]') # 빠진 부분에 대해서 하나 추가

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

df$temper = as.numeric(df$temper)
df$rain = as.numeric(df$rain)

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

library(dplyr)
library(tidyr)
#temp <- df %>% group_by(temper2, BRAND) %>%  tally() 행 갯수로 세는거
# sum으로 세기 전체 총합
temp <- df %>% group_by(temper2)  

brand_sum = aggregate(temp$QUANTITY, by=list(temp$temper2), FUN=sum)
names(brand_sum) = c('temper','sum')
ggplot(brand_sum, aes(temper, sum ))+geom_bar(stat="identity", position="dodge")

# brand별 총합
temper_brand_sum=df %>%group_by(temper2, BRAND) %>% summarise(a_sum=sum(QUANTITY))
ggplot(temper_brand_sum, aes(BRAND, a_sum ),fill=temper2)+geom_bar(stat="identity", position="dodge")
qplot(temper2, a_sum, data=temper_brand_sum, color=factor(BRAND), geom="bar")
ggplot(temper_brand_sum, aes(temper2 , a_sum, color=BRAND),fill = BRAND)+geom_bar(stat="identity", position="dodge")

#ggplot(temp, aes(temper2, n , fill = BRAND))+geom_bar(stat="identity", position="dodge")
ggplot(brand_sum, aes(BRAND, sum ))+geom_bar(stat="identity", position="dodge")

table(df$BRAND)
temp2 = subset(df,BRAND=='탕맛기픈')  
temp2 <- temp2 %>% group_by(temper2) %>%  tally()

ggplot(temp2, aes(temper2, n ))+geom_bar(stat="identity", position="dodge")
