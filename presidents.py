<<<<<<< HEAD
import pandas as pd

df=pd.read_excel('http://qrc.depaul.edu/Excel_Files/Presidents.xls')
#print(df['Political Party'].value_counts())
#matplotlib inline

df['Political Party'].value_counts().plot(kind="pie")
=======
import pandas as pd

df=pd.read_excel('http://qrc.depaul.edu/Excel_Files/Presidents.xls')
#print(df['Political Party'].value_counts())
#matplotlib inline

df['Political Party'].value_counts().plot(kind="pie")
>>>>>>> 18c0589cd863ddd50038bf9d112beb00982f3dfd
