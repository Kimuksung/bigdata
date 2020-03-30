#################################
## <제9장-1 연습문제>
################################# 

# 01. 다음과 같은 단계를 통해서 테이블을 호출하고, SQL문을 이용하여 레코드를 조회하시오.
# (DBMS : Oracle 사용)

conn<-dbConnect(drv, "jdbc:oracle:thin:@//127.0.0.1:1521/xe","scott","tiger")
query = "select * from tab"
dbGetQuery(conn,query)
dbSendUpdate(conn,query)

# [단계 1] 사원테이블(EMP)을 검색하여 결과를 EMP_DF로 변수로 불러오기
EMP_DF = dbGetQuery(conn,"select * from EMP")
str(EMP_DF)
# [단계 2] EMP_DF 변수를 대상으로 부서별 급여의 합계를 막대차트로 시각화

library(dplyr)

temp2 = EMP_DF%>%group_by(DEPTNO)
ggplot(temp,aes(x=x,Group.1))
ggplot(temp2,aes(x=DEPTNO,y=SAL,fill=DEPTNO)) +geom_bar(stat='identity')
ggplot(temp2,aes(x=DEPTNO,y=SAL,fill=factor(DEPTNO))) +geom_bar(stat='identity')

# [단계 3] 막대차트를 대상으로 X축의 축눈금을 부서명으로 표시하기
df = aggregate(EMP_DF$SAL, by=list(EMP_DF$DEPTNO), FUN=sum)
df$deptname[df$Group.1==10]="데이터"
df$deptname[df$Group.1==20]="클라우드"
df$deptname[df$Group.1==30]="블록체인"
df
ggplot(df,aes(x=deptname,y=x,fill=factor(deptname))) +geom_bar(stat='identity')




#-----------다른 풀이
emp_sal_tot = summarise(temp2,dept_tot=sum(SAL))
emp_sal_tot

# [단계 3] 막대차트를 대상으로 X축의 축눈금을 부서명으로 표시하기
# 부서 테이블 조회 
dept <- dbGetQuery(conn, "select * from dept")
# 부서명 추출 
dname <- dept$DNAME[1:3]

# x축 눈금(names.arg) : 부서명 표시 
barplot(emp_sal_tot$dept_tot, 
        col = rainbow(3),
        names.arg = dname)


# example date / 지역 / 성별 / 나이 
a = c("월" ,"서울", "남",24)
b = c("월" ,"경기", "여",55)
c = c("월" ,"서울", "남",35)

d = c("화" ,"서울", "여",19)
e = c("화" ,"경기", "여",23)
f = c("화" ,"서울", "남",39)

g = c("수" ,"서울", "남",17)
h = c("수" ,"서울", "여",21)
i = c("수" ,"서울", "여",33)
j = c("수" ,"서울", "남",28)

data = t(data.frame(a,b,c,d,e,f,g,h,i,j))
#dcast(data)
data = data.frame(data)
colnames(data) <- c("요일","지역","성별","나이")
rownames(data)<-c(1,2,3,4,5,6,7,8,9,10)
str(data)
class(data)

data$age = as.numeric(as.character(data$'나이'))
data
data$agelabel[data$age<20]=1
data$agelabel[data$age<30 & data$'age'>=20]=2
data$agelabel[data$age<40 & data$'age'>=30]=3
data$agelabel[data$age>40]=4
data
temp = data%>%group_by(요일,agelabel) %>%  tally()
#temp = data%>%group_by(agelabel) %>%  tally()
ggplot()
ggplot(df,aes(x='요일',y=count(agelabel))) +geom_bar(stat='identity')
barplot(temp$n | temp$'요일') 
        #col = rainbow(4))#,
        #names.arg = dname)