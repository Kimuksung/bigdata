-- ���� ���ǿ��� �ڽ��� ���� �̸��� �����ͺ��̽��� ����
use NEW
go



-- import ���̺� ����

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

-- ���߿� Į�� �Ӽ� �����ϱ�

-- bulk inesert�� �̿��� Monitoring1~3.csv ��뷮 ���� import 

bulk insert Monitoring
from 'C:\Monitoring1.txt'
with (
        codepage = 'RAW',
        firstrow = 1,          -- 1��° ���κ��� 
        maxerrors = 0,
        fieldterminator = ',', -- �ʵ� ������                
        rowterminator = '\n',  -- ���α����� 
        
        tablock
)

-- ������ Ȯ���ϱ� 

select top 10 *
from Monitoring
