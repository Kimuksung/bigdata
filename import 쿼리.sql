-- 현재 세션에서 자신이 만든 이름의 데이터베이스명 설정
use NEW
go



-- import 테이블 생성

create table Monitoring
(
        TDATE varchar(14) not null
        ,SUBCPID varchar(50)
        ,CARRIER varchar(50)
        ,MOCODE varchar(50)
        ,CNT int
        ,MOCODEDESC nvarchar(200)
        ,ISCRITICAL nvarchar(200)
        ,STATUS varchar(50)
        ,RESULT varchar(50)
)

-- 나중에 칼럼 속성 변경하기

-- bulk inesert를 이용해 Monitoring1~3.csv 대용량 파일 import 

bulk insert Monitoring
from 'C:\Monitoring1.txt'
with (
        codepage = 'RAW',
        firstrow = 1,          -- 1번째 라인부터 
        maxerrors = 0,
        fieldterminator = ',', -- 필드 구분자                
        rowterminator = '\n',  -- 라인구분자 
        
        tablock
)

-- 데이터 확인하기 

select top 10 *
from Monitoring
