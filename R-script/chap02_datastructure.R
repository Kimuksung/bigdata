# DataStructure

# 자료구조의 유형
# 1) Vector - 동일한 자료형을 가지는 1차원 배열 구조.
# 생성 함수: c() / seq() / rep()

x<- c(1,3,5,7)
y<- c(3,5)
length(x)

# 집합 관련 함수
union(x,y) #합집합
setdiff(x,y) # 차집합
intersect(x,y) #교집합

# 벡터 변수 유형
num <- 1:5
num
num <-c(-10:5)
num

# 벡터 원소 이름 지정
names <- c("kim","park","uk")
age <- c(27,25,31)
names(age) <- names
age
names

str(age)

#object의 자료구조를 알려준다. 아래와 같다면 vector 형식
#Named num [1:3] 27 25 31
#- attr(*, "names")= chr [1:3] "kim" "park" "uk"

# seq()
num<-seq(1,10,by=2)
num
num2<-seq(10,1,by=-2)
num2

# rep()
?rep
rep(1:3,times=3)
rep(1:3,each=3)

#----------------------------------------02.27
# data가 너무 많다면 아래것들이 잘려서 나오게 되는데 이 때 혀결 방법
# options(max.print = .Machine$integer.max)
# options(max.print = 9999999)

install.packages('stringr')
install.packages(url,repos=NULL) #현재 위치에 새로운 pakage를 설치

.libPaths()

library(stringr) #package memory upload

# memory loading 패키지 확인
search()

# 색인(index) : 저장 위치
# object[n]

a<- 1:50
a
a[c(10:15 , 30:35)] #여러 범위 지정

# 함수 이용
length(a)
a[10:(length(a)-5)]
a[seq(2,length(a),by = 2)]

# 특정 원소 제외(-)
a[-c(20:30)]

# 조건식
a[a>=10 & a<=30]
a[a<=10 | a>=30]
a[!(a>=10)]

# matrix - same data dtype by 2 demension
# how to use : matrix() , rbind() , cbind()
# function : apply()

m1 <- matrix(data=c(1:5)) # row : vector num , column : 1
m1
dim(m1) # row , column
mode(m1) # numberic
class(m1) # matrix

m2 <- matrix(data = c(1:9),nrow=3,ncol=3,byrow=T) # row first
m2
m3 <- matrix(data = c(1:9),nrow=3,ncol=3,byrow=F) # column first
m3

# rbind
x<- 1:5
y<- 6:10
z<- 11:15
w<- c('r','r','r','r','r')
m4 <- rbind(x,y)
m4 <- rbind(m4,z)
m4 <- rbind(m4,w)
m4

# cbind
m5 <- cbind(x,y,z,w)
m5

# matrix indexing
# object[row,column]

m6<- matrix(data = c(1:9),nrow=3,ncol=3)
m6
m6[2:3,1:2]

# 속성
m6[-2,]
m6[-1,-1]
m6[,-c(1,3)]

# row, column 이름 지정
colnames(m6) <- c("one","two","three")
m6
m6[,'one']
m6[,'one':'two'] # x 불가능
m6[,1:2] # o 

# broadcast 연산 low demension => big demension

x<- matrix(1:12,nrow=4,ncol=3, byrow=T)
x
# scala(0) * matrix(2)  - 작은 차원이 큰 차원으로 들어가게 된다.
0.5 * x
# vector(1) * matrix(2)
y<- 10:12
y+x
x

# matrix * matrix - 동일한 차원
x+x
x*x

# 전치 행렬 - 행 => 열 열 => 행
x
t(x)

# apply() : 처리 함수
help("apply")
apply(x,1,sum)
apply(x,2,mean)

# array 자료 구조
# - 3차원 배열 구조
# how to use: array()

arr <- array(data=c(1:12),dim=c(3,2,2)) #3 - 2 - 2로 만들어준다.
arr

data()
data("iris3")
iris3

dim(iris3) # 꽃이 3개 종류 각각의 넓이,높이,등등 4개 50개씩 조사

# array index
arr[,,1]
iris3[,,1]
iris3[,1,]
iris3[,,3]

# data frame - column 마다 다른 자로형을 가질 수 있다. 2차원 구조
# how to use? data.frame()
# function? apply() -> 행렬을 처리

#1) vector를 이용
no <- 1:3
name <- c("홍길동","이순신","유관순")
sal <- c(250,350,300)

emp <- data.frame( NO = no, Name = name ,Pay = sal)
emp
dim(emp)
class(emp)
mode(emp) #여러형의 자료형인 경우 list라 나온다.

#자료 참조 : column 대부분 index 가끔
# objects$column ex)emp$NO
pay <- emp$Pay
pay
mean(pay)
sd(pay)
# objects[row,column]
emp_row <- emp[c(1,3),] #특정행 추출출 emp[-2,]
emp_row
emp[2]

# csv / text file / db table
setwd("C:/ITWILL/2_Rwork/Part-I")

emp_txt <- read.table("emp.txt", header=T , sep="")  #text 불러오기
emp_txt
class(emp_txt) # dataframe

emp_csv <- read.csv("emp.csv")
emp_csv
class(emp_csv) # dataframe

###
sid <- 1:3 #학번
score <- c(90,85,83) #연속형
gender <- c('M','F','M')

student <- data.frame(SID=sid,Score=score,Gender=gender , stringsAsFactors = T) #false -> chr true-> factor
student

# 자료 구조 보기
str(student) 



# 특정 칼럼 -> vector
score <-student$Score
score

# List : key-value
# 1) key 생략: [key=value...]


lst <- list('lee','이순신',35,'hong','홍길동',30)
lst
lst[6]

#key -> value
lst[[5]]

# 2) key -value 형식
lst2 <- list(first= 1:5, second=6:10)
lst2$first
lst2$second
lst2$first[3]

# 3) 다양한 자료형
lst3 <- list(name=c('홍길동','김욱성'), age=c(33,27),gender=c('M','F'))
lst3$name[1]
mean(lst3$age) 

# 4) 다양한 자료구조
lst4 <- list(one = c('one','two','three'),
             two = matrix(1:9,nrow=3),
             three=array(1:12,c(2,3,2)) )
lst4
lst4$one
lst4$two
lst4$three

# 5) list 형 변환
multi_list <- list(r1=list(a=1,b=2,c=3),
                   r2=list(10,20,30),
                   r3=list(100,200,300)
                   )

multi_list$r1$a

# 중첩 list function 
# key말고 data만 보여주겠다.
mat <- do.call(rbind,multi_list)
mat

# list 처리 함수
x<- list(1:10)

#list -> vector
v <- unlist(x) # key 제거
a <- list(1:5)
b <- list(6:10)
a
b

#list 객체에 함수 적용
lapply(c(a,b),max) # list 반환
sapply(c(a,b),max) # vector 반환

# 산포도 : 분산 , 표준편차
# 모집단에 대한 분산 , 표준편차
# 분산 = sum((x-산술평균)^2)/n

# 표본에 대한 분산, 표준 편차 <- R
# 분산 = sum((x-산술평균&2))/n-1

# 이러한 이유 때문에 값이 조금 다르게 나올 수 있다.

# subset - 특정 row / column을 선택 => 새로운 dataset 생성
x<-1:5
y<-6:10
z<-letters[1:5]
df <- data.frame(x,y,z)
df
help("subset")

#subset(x, subset, select, drop = FALSE, ...)
#1) 조건식 : row 기준
df2<-subset(df,x>=2)
df2
#2) select : column 기준
df3<-subset(df,select=c(x,z))
df3
#3) 조건식 + select
df4<-subset(df,x>2 & x<=4, select=c(x,z))
df4
class(df2)
class(df3)
class(df4)
#4) 특정 column 특정 값으로 subset
subset(df,z %in% c('a','c','e'))
#subset(df,z in c('a','c','e')) X
