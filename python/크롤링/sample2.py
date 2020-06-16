import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# R의 dataframe을 가져와 만든것 -> pandas

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))
print(df.shape)

df = pd.DataFrame({"A":[1,4,7], "B":[2,5,8], "C":[3,6,9]})
## 첫 5개 행의 데이터를 보여줍니다.
print(df.head())
## 마지막 3개 행의 데이터를 보여줍니다.
print(df.tail(3))
##DataFrame의 인덱스를 보려면 .index 속성을, 컬럼을 보려면 .columns 속성을, 안에 들어있는 numpy 데이터를 보려면 .values 속성
print(df.index)
print(df.columns)
print(df.values)
##.describe() 메소드는 생성했던 DataFrame 의 간단한 통계 정보
print(df.describe())
## 열과 행을 바꾼 형태의 데이터프레임입니다.
print(df.T)
## A라는 이름을 가진 컬럼의 데이터만 갖고옵니다.
print(df['A'])
#라벨의 이름을 이용하여 선택할 수 있는 .loc

#konlpy설치 과정에서 pip upgrade error 원인 모르겟음 삭제햇다가 새로운 프로젝트에 재설치해야 할듯
from konlpy.tag import Komoran
komoran = Komoran()

