# chap09_1_Formal(2_Maria_DB)

# Maria DB 정형 데이터 처리

# 패키지 설치
# - RJDBC 패키지를 사용하기 위해서는 우선 java를 설치해야 한다.
#install.packages("rJava")
#install.packages("DBI")
#install.packages("RJDBC") # JDBC()함수 제공 

# 패키지 로딩
library(DBI)
Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre1.8.0_151')
library(rJava)
library(RJDBC) # rJava에 의존적이다.

################ MariaDB or MySql ###############
drv <- JDBC(driverClass="com.mysql.jdbc.Driver", 
            classPath="C:/ITWILL/2_Rwork/tools(R)/MariaDB/mysql-connector-java-5.1.46/mysql-connector-java-5.1.46/mysql-connector-java-5.1.46-bin.jar")

# driver가 완전히 로드된 후 db를 연결한다.
conn <- dbConnect(drv, "jdbc:mysql://127.0.0.1:3306/work", "scott", "tiger")
#################################################           

query = "show tables"
dbGetQuery(conn,query)

dbGetQuery(conn,"select * from goods")

#DB 구조 변경
dbSendUpdate(conn,"insert into goods values (5,'컴퓨터', 4, 700000)")
dbSendUpdate(conn,"update goods set dan=800000 where code=5 ")
dbSendUpdate(conn,"delete from goods where name='컴퓨터' ")

goods = dbGetQuery(conn,"select * from goods")
str(goods)

goods$price = goods$su*goods$dan

write.csv(goods,"goods.csv",quote=F,row.names = F)

dbSendUpdate(conn,"drop table goods_manager")
#table save
"create table goods_manager(code int ,name varchar(50),su int ,dan int ,price int)"
dbSendUpdate(conn, "create table goods_manager(code int ,name varchar(50),su int ,dan int ,price int)")
dbGetQuery(conn,"show tables")
dbWriteTable(conn,name ="goods_manager" ,value = goods )
dbGetQuery(conn,"select * from goods_manager")

dbDisconnect(conn)

