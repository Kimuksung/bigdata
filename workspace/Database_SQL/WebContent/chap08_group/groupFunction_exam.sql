/*
 * 집합 함수(COUNT,MAX,MIN,SUM,AVG) 
 * 작업 대상 테이블 : EMP, STUDENT, PROFESSOR
 */

--Q1. EMP 테이블에서 소속 부서별 최대 급여와 최소 급여 구하기
select min(sal),max(sal) from emp;
--Q2. EMP 테이블에서 JOB의 수 출력하기
select count(*) from emp group by job;

--Q3. EMP 테이블에서 전체 사원의 급여에 대한 분산과 표준편차 구하기
select variance(sal) from emp;
select stddev(sal) from emp;
--Q4. Professor 테이블에서 학과별 급여(pay) 평균이 400 이상 레코드 출력하기
select deptno from professor group by deptno having avg(pay)>=400;
--Q5. Professor 테이블에서 학과별,직위별 급여(pay) 평균 구하기
select deptno,position,avg(pay) as deptnoavg from professor group by deptno,position;
select * from (select * as deptavg from professor group by deptno),
(select * as posavg from professor group by position);

purge recyclebin;
create table professor2 as (select position as "직책",avg(pay) as "월급"  from professor group by position);
create table professor3 as (select deptno as "부서",avg(pay) as "부서월급"  from professor group by deptno);
select * from professor2;
select * from tab;
select * from professor3;
select * from professor;
drop table professor3;
SELECT deptno,avg(pay) as deptpay
FROM professor
group by deptno

outer join
professor2;

select distinct(a.부서),a.부서월급,b.직책,b.월급 from professor3 a,professor2 b;
/*
SELECT position as positionpay
FROM professor2
group by position; 
*/

--Q6. Student 테이블에서 학년(grade)별로 
-- weight, height의 평균값, 최대값, 최소값을 구한 
-- 결과에서 키의 평균이 170 이하인 경우 구하기
select grade from student group by grade having avg(height)<=170;
