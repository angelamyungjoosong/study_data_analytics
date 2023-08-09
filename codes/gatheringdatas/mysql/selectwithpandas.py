# mysql connect package

# pip (퓨어자바에서 스토어를 연결하는 명령어) 대신 conda 사용 
import pymysql  

# connect Mysql

# ip, port, username, password, database name : 연결할 때 필요한 5가지 
ip = 'localhost'    #127.0.0.1
port = '3306' #default(안써도됨)
username = 'root'
password = '!yojulab*'
database = 'db_cars'

# editor화면 - statement  
connect = pymysql.connect(host=ip, user=username, password=password, database=database) #pymysql은 class로 connect라는 function사용 #host,user는 parameter이름 (java에서는 순서대로 넣었지만 파이썬에서는 특정parameter이름과 내가 만든 parameter매칭시켜줄 수 있다 ) #port는 3306이 default(안써도됨)
    # (앞의 connect가 statement. statement에 쿼리문 올리는 것)

# make select statement 
sql_query = 'SELECT * FROM car_infors;'

# execute select query 
import pandas 
    #데이터를 가져오는데 쓰는 프로그램 


#return resultset and then display
df = pandas.read_sql(sql=sql_query, con=connect) 
    # 연결 후 리턴을 받을때 df라는 변수를 씀(data frame)
    # df에 자료가 담긴 상태 

#close 
connect.close()  #connection 종료 

pass

# print(df)
# CAR_NAME  YEAR CAR_INFOR_ID COMPANY_ID
# 0       소나타  2020        CI001       C001
# 1       쏘렌토  2021        CI002       C002
# 2       SM6  2019        CI003       C003
# 3     3 시리즈  2022        CI004       C004
# 4        캠리  2020        CI005       C005
# ..      ...   ...          ...        ...
# 63       투싼  2021        CI103       C002
# 64      셀토스  2022        CI104       C002
# 65      SM6  2019        CI105       C003
# 66      SM3  2020        CI106       C003
# 67    3 시리즈  2022        CI107       C004

# [68 rows x 4 columns]

