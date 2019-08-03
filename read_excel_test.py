import pandas as pd
sales=pd.read_excel('C:/Python_Practice/raw_data_hospital.xlsx',sheet_name=
                    'list')

print(sales['의료기관종별'])
print(sales['의료기관명'])
print(sales['의료기관주소(도로명)'])
print(sales['의료기관전화번호'])
      
