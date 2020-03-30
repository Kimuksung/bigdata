#################################
## <제8장 연습문제>
################################# 

#01. 다음 조건에 맞게 airquality 데이터 셋의 Ozone과 Wind 변수를 대상으로  
# 다음과 같이 산점도로 시각화 하시오.

#조건1) y축 : Ozone 변수, x축 : Wind 변수 
xyplot(Ozone ~ Wind, data=airquality) 
#조건2) Month 변수를 factor형으로 변경  
 
#조건3) Month 변수를 이용하여 5개 격자(lattice)를 갖는 산점도 그래프 그리기
library(lattice)
xyplot(Ozone ~ Wind | factor(Month), data=airquality)
head(airquality)
str(airquality)

#------------
air_df = transform(airquality,Month=factor(Month))
str(air_df)
xyplot(Ozone ~ Wind | factor(Month), data=air_df)
# 02. 서울지역 4년제 대학교 위치 정보(Part-II/university.csv) 파일을 이용하여 레이어 형식으로 시각화 하시오.

# 조건1) 지도 중심 지역 SEOUL, zoom=11
# 조건2) 위도(LAT), 경도(LON)를 이용하여 학교의 포인트 표시
# 조건3) 각 학교명으로 텍스트 표시
# 조건4) 완성된 지도를 "university.png"로 저장하기(width=10.24,height=7.68) 
library(ggmap)
setwd("C:/ITWILL/2_Rwork/Part-II")
temp =read.csv('university.csv')
temp
seoul <- c(left = 126.85, bottom = 37.35, 
           right = 127.25, top = 37.65)
temp1 = get_stamenmap(seoul,zoom = 11 ,maptype='watercolor')
ggmap(temp1)

region = temp$'학교명'
lon = temp$'LAT'
lat = temp$'LON'
df= data.frame(region,lon,lat)
df
layer2 = layer1 + geom_point(data=df,mapping= aes(x=lon,y=lat,size=factor(region)))
#layer2 = layer1 + geom_point(data=df,aes(x=lon, y=lat,color=factor(tot_pot),size=factor(tot_pot)))
layer2
layer3 = layer2 + geom_text(data = df, aes(x = lon, y = lat+0.01, label = region), size=3)
layer3
