-- dataType.sql : Oracle 주요 자료형 

create table student(
sid int primary key,            -- 학번 
name varchar(25) not null,  -- 이름 
phone varchar(30) unique,  -- 전화번호
email char(50),                  -- 이메일 
enter_date date not null     -- 입학년도 
);


/*
 * Oracle 주요 자료형 
 *  1. number(n) : n 크기 만큼 숫자 저장 
 *  2. int : 4바이트 정수 저장 
 *  3. varchar2(n) : n 크기 만큼 가변길이 문자 저장 
 *  4. char(n) : n 크기 만큼 고정길이 문자 저장
 *  5. date : 날짜/시간 저장 - sysdate : system의 날짜/시간 저장 
 */

/*
 * 제약조건 
 *  1. primary key : 해당 칼럼을 기본키로 지정(중복불가+null불가)
 *  2. not null : null값 허용 불가 
 *  3. unique : 중복 불가(null 허용)
 */

/*
 * sequence?
 *  - 시작값을 기준으로 일정한 값이 증가하는 객체 
 *  - 형식) create sequence 이름 increment by 증가값 start with 시작값;
 */

create sequence seq_sid increment by 1 start with 2000;
insert into student values(seq_sid.nextval,'김욱성','010-4393-9492','kimuksung2@daum.net',sysdate);
select * from student;
insert into student values(seq_sid.nextval,'이순신','010-2312-9492','lee@naver.com',sysdate);
insert into student values(seq_sid.nextval,'장보고','010-1242-9492','kimuksung2@google.com',sysdate);
insert into student values(seq_sid.nextval,'김남준','010-1243-2312','kimnam@google.com',sysdate);

--제약 조건 위배
insert into student values(seq_sid.nextval,'박박박','010-1243-2312','kimnam@google.com',sysdate);

select * from tab;
-- db에 작업 내용 반영
commit work;

-- 재시작

drop table student purge;
create table student(
sid int primary key,            -- 학번 
name varchar(25) not null,  -- 이름 
phone varchar(30) unique,  -- 전화번호
email char(50),                  -- 이메일 
enter_date date not null     -- 입학년도 
);

drop sequence seq_sid;
create sequence seq_sid increment by 1 start with 2000001;

insert into student values(seq_sid.nextval,'김욱성','010-4393-9492','kimuksung2@daum.net',sysdate);
insert into student values(seq_sid.nextval,'이순신','010-2312-9492','lee@naver.com',sysdate);
insert into student values(seq_sid.nextval,'장보고','010-1242-9492','kimuksung2@google.com',sysdate);
insert into student values(seq_sid.nextval,'김남준','010-1243-2312','kimnam@google.com',sysdate);
select * from student;
