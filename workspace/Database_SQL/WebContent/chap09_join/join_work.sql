/*
	-특정 칼럼(외래키)를 이용하여 2개 이상의 table을 연결
	
	절차
	1. 기본키를 갖는 table 생성
	2. 레코드 추가
	3. 외래키를 갖는 테이블 생성
	4. 레코드 추가

	조인 테이블 삭제 : 위 순서를 역순으로 하면 된다.
	강제 테이블 삭제 : drop table a cascade constraint;
*/

drop table product;

create table product(
code char(4) primary key,
name varchar(30) not null
);

insert into product values ('p001','냉장고');
insert into product values ('p002','세탁기');
insert into product values ('p003','전화기');

select * from product;

create table sale(
code char(4) not null,
sdate date not null,
price int not null,
foreign key(code) references product(code)
);


insert into sale values('p001','2020-02-24',1000000);
insert into sale values('p002','2020-02-25',7500000);
insert into sale values('p003','2020-02-27',500000);
insert into sale values('p001','2020-02-26',4000000);
insert into sale values('p002','2020-02-22',2000000);

select * from sale;
--insert into sale values('p006','2020-02-24',1000000);
commit work;

select * from product p,sale s where p.code=s.code and p.name like '%기';

/* cartesian join : 물리적 join 없이 논리적으로 테이블을 연결하는 기법(공통 칼럼 기준)
	1. inner join
		- table끼리 공통적인 data가 있어야 한다.
	2. outer join
		- 하나의 table에만 data가 존재하는 경우이다.
		- left outer join / right outer join / full outer join
*/

-- inner join = > 학생 + 학과
select * from department;
select * from student;
select * from student , department where student.deptno1 = department.deptno;

-- ANSI 표준 : inner join
select * from student inner join department on student.deptno1 = department.deptno;

-- 학생 table 교수 table
select * from student;
select * from professor;
select s.name,s.deptno1,p.name,p.profno from student s,professor p where s.profno = p.profno;

-- 101학과 학생만 검색하라
select s.name,s.deptno1,p.name,p.profno from student s,professor p where s.profno = p.profno and s.deptno1=101;

-- 3개 이상의 table join => 학생 + 학과 + 교수
select * from student;
select * from professor;
select s.name,d.deptno,f.profno from student s,department d,
professor f where s.deptno1=d.deptno and f.profno=s.profno;

-- outer join => 학생 + 교수
select s.name,p.name from student s ,professor p where s.profno = p.profno(+);

-- ansi 표준
select s.name,p.name from left student s outer join professor p on s.profno = p.profno;