select * from tab;

SELECT * FROM emp;

select empno, ename, sal, job from emp;

select empno, ename, sal*12 as year, job from emp;

select ename, sal, sal*1.1 from emp;

SELECT empno, ename, sal, comm, sal+comm/100 FROM emp; -- 하나라도 null이 속해잇다면 값도 null로 출력

SELECT empno, ename, sal, comm, (sal+NVL(comm,0))/100 FROM emp; --null 처리 해주어야 한다.

SELECT empno, ename, sal*12+NVL(comm,0) as year FROM emp;

select ename || '/' ||job as employees from emp;
select ename || '/' ||job as "근 로 자" from emp; --띄어쓰기하고싶으면 ""

SELECT DISTINCT deptno, job FROM emp order by deptno desc;

select empno,ename,job,sal,hiredate,deptno from emp
where hiredate >= to_date('1982/01/01', 'yyyy/mm/dd');

select * from emp where hiredate 
between to_date('19820101', 'YYYYMMDD') and to_date('19821231', 'YYYYMMDD');

select * from emp where ename like 'M%R%';

--문) 부서번호 deptno가 10번이고, 급여가 2500이상 사원 조회
select * from emp where deptno=10 and sal>=2500;

--문) 직책이 사원이거나 부서번호가 30인 사원 조회
select * from emp where job='CLERK' or deptno=30;

select * from emp;
select ename,deptno from emp where deptno = (select deptno from emp where ename='SCOTT');
select * from emp where mgr = (select mgr from emp where ename='SCOTT');