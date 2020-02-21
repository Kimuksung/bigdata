/*
 * DDL : table create update delete
 * ddl 실행 시 -> auto commit
 */

-- 의사 컬럼(rownum,rowid)
-- webpage 긁어오거나 할 때 사용
--1) row num : 레코드 순번
--문제점 관계식 논리식이 적용되지 않는다. and / or / 등등

SELECT ROWNUM, EMPNO, ENAME, ROWID
FROM EMP WHERE ROWNUM <=10 ;

SELECT ROWNUM, EMPNO, ENAME, ROWID
FROM EMP WHERE ROWNUM >=5 and ROWNUM <=10 ;

-- 대안으로 subquery를 이용한 별칭
select rnum, EMPNO, ENAME
from (select EMPNO,ENAME,ROWNUM as rnum from emp)
where rnum>=5 and rnum<=10;

-- 실수형 데이터 저장 테이블
drop table emp01 pruge;
CREATE TABLE EMP01(
EMPNO NUMBER(4),
ENAME VARCHAR2(20),
SAL NUMBER(7, 2));

insert into emp01 values (1,'홍길동',1234.1);
insert into emp01 values (2,'김욱성',1234.123);
insert into emp01 values (3,'김남준',1234.125);
insert into emp01 values (4,'박정연',12345678.125123);
select * from emp01;

-- 서브쿼리 이용한 테이블
create table emp02 as select * from emp;
select * from emp02;

-- 특정 칼럼 내용 복제
create table emp03 as select EMPNO, ENAME FROM EMP;
select * from emp03;

create table emp04 as select empno,ename,sal from emp;
select * from emp04;

-- 구조 복제 테이블 생성
CREATE TABLE EMP05 AS
SELECT * FROM EMP WHERE DEPTNO=10;

select * from emp05;

-- 문제 직책이 관리자만 대상으로 테이블 생성(EPM_TEST)
create table emp_test as select * from emp where job='MANAGER';
select * from emp;
select * from emp_test;

--table 구조만 복사하기(조건을 false로 하면 된다)
CREATE TABLE EMP06
AS
SELECT * FROM EMP WHERE 0=1;

select * from emp06;
drop table emp06 purge;

create table dept02 as select * from dept where 0=1;
select * from dept02;

-- 제약 조건
-- 1) primary key

create table test_tab1(
id number(2) primary key,
name varchar(30)
);

insert into test_tab1 values(11,'홍길동');
insert into test_tab1 values(22,'유관순');
insert into test_tab1 (name )values('홍길동');--불가

-- 외래키 기본키 테이블 생성->외래키 테이블 생성
drop table emp_tap purge;

create table dept_tap(
	deptno number(2) primary key,
	dname varchar(10) not null,
	loc varchar(10) not null
);

insert into dept_tap values (1,'기획실','대전' );
insert into dept_tap values (2,'총무','서울' );
insert into dept_tap values (3,'개발','중국' );

select * from dept_tap;

create table emp_tap(
	empno number(4) ,
	ename varchar(25),
	sal number(7),
	deptno number(2) not null,
	foreign key(deptno) references dept_tap(deptno)
);

insert into emp_tap values (2013,'김욱성',1000,1 );
insert into emp_tap values (2014,'김남준',500,2 );
insert into emp_tap values (2013,'박정연',700,3 );
insert into emp_tap values (2013,'허강무',400,4 );
select * from emp_tap;

-- 문) 서브쿼리를 이용하여 2013 사번을 갖는 사원의 부서 출력하기
select dname from dept_tap where deptno in
(select deptno from emp_tap where empno=2013);

create table test_tab2(
id number(2) ,
name varchar(30),
primary key(id)
);


-- 유일키 unique
-- not null comlumn 내에서만 가능하다.

CREATE TABLE CK_TAB1 (
DEPTNO NUMBER(2) NOT NULL CHECK (DEPTNO IN (10,20,30,40,50)),
DNAME CHAR(14),
LOC CHAR(13));

INSERT INTO CK_TAB1 VALUES(10,'AAAA','BBBB');
INSERT INTO CK_TAB1 VALUES(60,'AAAA','BBBB');

-- 5. 테이블 구조 변경(alter table)
select * from emp01;
alter table emp01 add(job3 varchar(10)); --not null 불가
alter table emp01 add(job4 varchar(10) default);


alter table emp01 modify(job3 not null);


select * from dept02;
alter table dept02 add(DMGR varchar(20));
alter table dept02 modify(DMGR number(4));
ALTER TABLE dept02
DROP COLUMN DMGR;
desc dept02;

-- 다중 테이블 다중 행

create table EMP_HIR as select EMPNO, ENAME, HIREDATE from emp
where 0=1;
create table EMP_MGR as select EMPNO, ENAME, MGR from emp
where 0=1;
select * from EMP_HIR;
select * from EMP_MGR;

insert all
into EMP_HIR values(EMPNO, ENAME, HIREDATE) 
INTO EMP_MGR VALUES(EMPNO, ENAME, MGR)
SELECT EMPNO, ENAME, HIREDATE, MGR
FROM EMP
WHERE DEPTNO=20;

--update

select * from emp01;
alter table emp01 drop column JOB3;
alter table emp01 add (deptno number(4));
alter table emp01 add (HIREDATE date);
update emp01 set deptno=30;
UPDATE EMP01 SET SAL = SAL * 1.1;
UPDATE EMP01 SET HIREDATE = SYSDATE; 

select * from sam01;
update sam01 set sal=sal-5000 where sal>10000;

select * from sam02;
drop table sam02;
create table sam02 as select ename,sal,hiredate,deptno from emp;

select * from dept;
update sam02 set sal=sal+1000 where deptno=(select deptno from dept where loc='DALLAS' );


update sam02 set (sal,hiredate) 
= (select sal,hiredate from sam02 where ename='KING');

select * from sam01;
delete from sam01 where job is null;

select * from emp01;