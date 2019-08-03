#판다스를 임포트
import pandas as pd

#csv파일을 읽어 온다.
df=pd.read_csv("mtcars.csv")

#head()함수는 데이터의 맨 앞부분 5개를 보여줌.
#df.tail()은 데이터의 뒷부분 5개를 보여준다.

#print(df.head())

#특정 범위의 관측치만 보고 싶다면 행에 대해 슬라이씬하라...

#print(df[0:2])

#변수명만 따로 살펴 보기.
#print(df.columns)

#
print(df.describe())
