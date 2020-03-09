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











