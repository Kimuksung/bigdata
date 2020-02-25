-- view : virtual table

create table db_view_tab(
	id varchar(15) primary key,
	name varchar(20) not null,
	email varchar(50),
	regdate date not null
);

insert into db_view_tab values ('hong','홍길동','aaaa',sysdate);
insert into db_view_tab values ('admin','김욱성','admin',sysdate);
select * from db_view_tab;
commit work;


-- 읽기 전용 view
create or replace view admin_view as select * from db_view_tab where id='admin' with read only;
-- view 목록 확인
select * from user_views;

select * from admin_view;

-- view 삭제
drop view admin_view;

select * from emp;
create view emp_view30 as select ename,empno,deptno from emp where deptno=30 with read only;
select * from emp_view30;

-- view 사용 용도 목적
/*
	1. 복잡한 sql문 사용 시
	2. 보안 목적 : 접근 권한
*/

select * from product;
select * from sale;

create or replace view join_view as 
(select p.code , p.name, s.price, s.sdate from product p , sale s where p.code=s.code and p.name like '%기')
with read only;

select * from join_view;


-- 보안 목적
select * from emp;

create or replace view sales_view as 
	select empno,ename,comm from emp where job='SALESMAN' order by comm desc  with read only; --view에서는 order by 사용하지 않는 것을 추천

select * from sales_view;

select * from emp;
create or replace view manager_view as(
	select empno,ename,comm from emp where job='SALESMAN' or job='ANALYST' or job='CLERK'
) with read only;

select * from manager_view;

-- 의사 컬럼(rownum) 이용 view 생성
=============
-- 최초 입사자 top5 / 급여 수령자 top3
---------------
select rownum,empno,ename from emp
where rownum <= 5;

-- 입사일 top5 view 생성
---------------
create or replace view top5_hire_view
as select empno,ename,hiredate
from emp where rownum<=5 order by hiredate asc with read only;

select * from top5_hire_view;

select * from emp;

--top3 연봉 생성
--2단계로 나누어서 할것
----------

#create or replace view top3_sal_view
#as select ename,job,sal from emp order by sal desc with read only; 
#select * from top3_sal_view;

#select rownum,ename,job,sal from top3_sal_view where rownum<=3;

