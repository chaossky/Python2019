import pandas as pd

df=pd.read_excel('http://qrc.depaul.edu/Excel_Files/Presidents.xls')
#print(df['Political Party'].value_counts())
#matplotlib inline

df['Political Party'].value_counts().plot(kind="pie")
