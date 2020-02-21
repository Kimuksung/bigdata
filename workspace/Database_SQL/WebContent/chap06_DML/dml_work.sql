--DML

/*
 
DML : select insert update delete
commit 대상 : insert update delete

*/


drop table dept01;
CREATE TABLE DEPT01(
DEPTNO NUMBER(4),
DNAME VARCHAR2(30),
LOC VARCHAR2(20)
);

INSERT INTO DEPT01 (DEPTNO, DNAME, LOC)
VALUES(10, 'ACCOUNTING', 'NEW YORK');

INSERT INTO DEPT01
VALUES (20, 'RESEARCH', 'DALLAS'); 

create table sam01 as select empno,ename,job,sal from emp;
select * from sam01;
TRUNCATE table sam01;
insert into sam01 values (1000,'APPLE','POLICE',10000);
insert into sam01 values (1010,'BANANA','NURSE',15000);
insert into sam01 values (1020,'DOCTOR','DOCTOR',25000);
insert into sam01 values (1030,'VERY',null,25000);
insert into sam01 (empno,ename,sal)values (1040,'cat',2000);

insert into sam01 select 
empno,ename,job,sal from emp where deptno=10;

DROP TABLE DEPT02;
select * from dept02;
CREATE TABLE DEPT02
AS
SELECT * FROM DEPT WHERE 1=0;
INSERT INTO DEPT02 SELECT * FROM DEPT;
CREATE TABLE DEPT02 as INSERT INTO DEPT02 SELECT * FROM DEPT;
