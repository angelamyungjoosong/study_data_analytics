# 리스트로 이름을 모두 가져오기 
# hint: 성씨 컬럼에 Null 없애야 함. 

import pandas as pd
df_TFD = pd.read_csv('./datasets/TitanicFromDisaster_train.csv')

df_Name = pd.DataFrame(df_TFD['Name'])

pattern = r'^([A-z]+)'
df_Name['LastName']= df_Name['Name'].str.extract(pattern)
print(df_Name['LastName'])
print(df_Name['LastName'].isnull().sum()) 


pattern = r'([A-Za-z]+\.)'
df_Name['Title'] = df_Name['Name'].str.extract(pattern)
print(df_Name['Title'])
print(df_Name['Title'].isnull().sum())