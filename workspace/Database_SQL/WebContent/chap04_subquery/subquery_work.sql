--subquery

/* 

형식1)
main query as sub query;

형식2)
main query 관계연산자 (sub query);

*/

--ex1)
create table dept01 as select * from dept;

select * from dept01;

--ex2)
select * from dept where deptno = 
(select deptno from emp where ename='SCOTT');

--단일행
/*
1. SCOTT과 같은 부서에서 근무하는 사원의 이름과 부서 번호를 출력
하는 SQL 문을 작성해 보시오. (EMP)
*/
select ename,deptno from emp where deptno=
(select deptno from emp where ename='SCOTT');

/*
2. SCOTT와 동일한 직속상관(MGR)을 가진 사원을 출력하는 SQL 문을
작성해 보시오. (EMP)
*/

select * from emp where mgr 
= (select mgr from emp where ename='SCOTT');

/*
3. SCOTT의 급여와 동일하거나 더 많이 받는 사원 명과 급여를 출력하
시오.(EMP)
*/
select * from emp where
sal >= (select sal from emp where ename='SCOTT');

/*
4. DALLAS에서 근무하는 사원의 이름, 부서 번호를 출력하시오.
(서브쿼리 : DEPT01, 메인쿼리 : EMP)
*/
select * from DEPT01;
select ename,deptno from emp where deptno=
(select deptno from DEPT01 where LOC='DALLAS');

/*
5. SALES(영업부) 부서에서 근무하는 모든 사원의 이름과 급여를
출력하시오.(서브쿼리 : DEPT01, 메인쿼리 : EMP
*/
select ename,sal from emp where deptno=
(select deptno from dept01 where dname='SALES');

/*
6. 연구분서('RESEARCH')에서 근무하는 모든 사원 정보 출력하세요.
*/
select * from emp where deptno=
(select deptno from dept01 where dname='RESEARCH');
select * from emp;

--평균이하 급여 수령자
select sal from emp where sal<(select avg(sal) from emp);

--다중행 서브쿼리(IN,ANY,ALL)

-- 1) IN
SELECT ENAME, SAL, DEPTNO FROM EMP
WHERE DEPTNO IN (SELECT DEPTNO FROM EMP WHERE SAL>=3000);

/*
7. 부서별로 가장 급여를 많이 받는 사원의 정보(사원 번호, 사원이름,
급여, 부서번호)를 출력하시오.(IN, MAX 연산자와 GROUP BY 이용)
*/
select * from emp;
select * from emp where (sal,deptno) IN
(select max(sal) , deptno from emp group by deptno);

/*
 8. 직급(JOB)이 MANAGER인 사람이 속한 부서의 부서 번호와
부서명과 지역을 출력하시오.(DEPT01과 EMP 테이블 이용)
*/

select deptno from emp where deptno in
(select deptno from dept01 where job='MANAGER');

select * from dept01;

/*
 9. 영업 사원('SALESMAN')들 보다 급여를 많이 받는 사원들의 이름과 급여와 직급
(담당 업무)를 출력하되 영업 사원은 출력하지 않습니다. 
*/
select * from emp;
select ename,sal,job from emp where sal>
all(select max(sal) from emp where job='SALESMAN' ) order by
sal;

/*
10. 영업 사원들의 최소 급여를 많이 받는 사원들의 이름과
급여와 직급(담당 업무)를 출력하되 영업 사원은 출력하
지 않습니다. 
*/
select * from emp;
select ename,sal,job from emp where sal <
any(select sal from emp where job='SALESMAN') order by sal desc;