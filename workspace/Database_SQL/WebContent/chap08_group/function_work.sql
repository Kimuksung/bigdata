	-- group function
select sum(comm) from emp;
select avg(comm) from emp; 

select round(avg(sal),1) from emp;
select avg(comm) from emp where comm>0;

select max(sal) from emp;
select max(hiredate) from emp;
select min(hiredate) from emp;
select * from emp;

select count(*) from emp where deptno=10 and comm is not null;
select count(distinct job) from emp;

select sum(sal),avg(sal),count(*) from emp where deptno=(select deptno from emp where ename='SCOTT') and ename != 'SCOTT';
select * from emp;

-- 분산 처리
-- 분산 = 편차^2 총합 / 갯수
select variance(pay) from professor; 
-- 표준편차 : 분산의 양의 제곱
select stddev(pay) from professor;
select * from professor;

-- group by
select deptno from emp group by deptno;
select sum(sal),avg(comm) from emp group by deptno;

select position,avg(pay) from PROFESSOR group by position;

-- having
select deptno,avg(sal) from emp group by deptno having avg(sal)>=2000;

select * from student;
select grade,avg(weight) from student group by grade having avg(weight)>=60;

select deptno from professor group by deptno having avg(pay)<300;
