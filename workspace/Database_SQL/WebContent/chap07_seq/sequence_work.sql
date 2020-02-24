--table create

select * from dept01;
drop table dept01 purge;

create table dept01 as select * from dept where 0 = 1;

create sequence seq1;

CREATE SEQUENCE DEPT_DEPTNO_SEQ
INCREMENT BY 1
START WITH 1;

-- sequence record insert

insert into dept01 values
(DEPT_DEPTNO_SEQ.nextval,'test1','서울시');
insert into dept01 values
(DEPT_DEPTNO_SEQ.nextval,'test2','대전시');

-- sequence 목록 보기
select * from USER_SEQUENCES;

--test 목적
SELECT DEPT_DEPTNO_SEQ.NEXTVAL FROM DUAL;

-- 실습 
CREATE SEQUENCE EMP_SEQ
START WITH 1
INCREMENT BY 1
MAXVALUE 100000 ; 

DROP TABLE EMP01;
CREATE TABLE EMP01(
EMPNO NUMBER(4) PRIMARY KEY,
ENAME VARCHAR2(10),
HIREDATE DATE
);

INSERT INTO EMP01
VALUES(EMP_SEQ.NEXTVAL, 'JULIA1' , SYSDATE);
INSERT INTO EMP01
VALUES(EMP_SEQ.NEXTVAL, 'JULIA2' , SYSDATE);

delete from emp01 where empno=2;
select * from emp01;

INSERT INTO EMP01
VALUES(EMP_SEQ.NEXTVAL, 'JULIA2' , SYSDATE);


drop table board purge;
purge recyclebin;
create table board (
	bno varchar(20) primary key,
	writer varchar(20) not null	
);

create sequence bno_seq start with 1001 increment by 1;

insert into board values 
('홍길동'||to_char(bno_seq.nextval),'홍길동');

insert into board values 
('이순신'||to_char(bno_seq.nextval),'이순신');
insert into board values 
('김욱성'||to_char(bno_seq.nextval),'김욱성');

select * from board;


-- function
-- 1. 숫자 처리

SELECT MOD (27, 2), MOD (27, 5), MOD (27, 7)
FROM DUAL;

select * from professor where mod(deptno,2)=0;
select * from emp where mod(empno,2)=1;

-- 2. 문자 처리
SELECT 'Welcome to Oracle', UPPER('Welcome to Oracle')
FROM DUAL;
SELECT 'Welcome to Oracle', LOWER('Welcome to Oracle')
FROM DUAL;
SELECT 'WELCOME TO ORACLE',
 INITCAP('WELCOME TO ORACLE')
FROM DUAL;

SELECT EMPNO, ENAME, JOB
FROM EMP
WHERE JOB=UPPER('manager');


select length(ename),lengthb(ename) from emp;

SELECT SUBSTR('Welcome to Oracle', 4, 3)
FROM DUAL;

select * from student;
select * from student where substr(to_char(birthday),1,2)='75';
select * from student where substr(to_char(birthday),4,2)='10';

select * from emp where substr(to_char(hiredate),4,2)='09';
select * from emp where substr(hiredate,4,2)='09';

SELECT RTRIM(' Oracle '),LTRIM(' Oracle '),TRIM(' Oracle ')
FROM DUAL;
SELECT SYSDATE-1 어제, SYSDATE 오늘, SYSDATE+1 내일
FROM DUAL;


SELECT SYSDATE, NEXT_DAY(SYSDATE, '수요일')
FROM DUAL;

SELECT TO_NUMBER('20,000', '99,999') - TO_NUMBER('10,000', '99,999')
FROM DUAL;

--NUll 처리
/*
1. NVL(칼럼,값) : 해당 칼럼명 값이 NULL-> 값 대체
2. NVL2(칼럼명,값1,값2) : 칼럼명이 NULL -> 값2 , NOT NULL -> 값1

*/

select name,pay,bonus,nvl2(bonus,bonus,0) from professor where deptno=101;

-- decode() 함수
-- decode(칼럼명,값,디코딩 내용)
select
  ename,
  deptno,
  decode(deptno, 10, '기획실', 20, '연구실', '영업부') as "부서명"
from
  emp;

  
  
  
  
