import pandas as pd

double_list = [
             [1000, '과자','2019-12-31','반품'],
             [2000, '음료', '2020-03-02', '정상'],
             [3000, '아이스크림', '2020-02-03','정상'],
             [1000,'과자','2019-12-31','반품']
            ]

double_columns = ['가격','종류','판매일자','반품여부']
df_saledays = pd.DataFrame(data=double_list, columns=double_columns)
df_saledays
# print(df_saledays)

#단일변수 처리 with apply()
def mean_subtraction(cell_value) :
    result = 1750 - cell_value  # 가격 평균 - 개별값
    return result

mean_subtraction(750)

df_saledays['가격'].apply(mean_subtraction)  # 각 cell당 평균 차이값
#시리즈로 가져온 경우 


#다변수 처리 with apply()
def calculate_sum(row):
    result = row['가격'] * 20 
    return result

df_saledays['가격합'] = df_saledays.apply(calculate_sum, axis='columns')
#전체를 다 가져와서 골라서 쓸 수있다 
#row가 레코드 하나씩으로 들어온다 
#return을 던질때는 범주형으로 던지면 가상 테이블에 쌓이게 된다
#꼭 row 아니어도 된다 

print(df_saledays)

#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html


#regexpress(정규식)
data = {'Names': ['김지수', '박지민', '이태용', '최수영']}

df_Name = pd.DataFrame(data)

print(df_Name)

pattern = r'^([가-힣])'

df_Name_extract = df_Name['Names'].str.extract(pattern)
print(df_Name_extract)