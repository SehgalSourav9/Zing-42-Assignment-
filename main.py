import os
import pandas as pd
from utilities import *
from sqlalchemy import create_engine
from pandas.io import sql

#First CSV File (Securities available for Equity segment (.csv))
data_1=pd.read_csv("https://archives.nseindia.com/content/equities/EQUITY_L.csv")

# Fetch bhavcopy files of last 30 days
path=os.getcwd()
data_dates=makeBhavCopies(path)

#Latest bhavcopy file
file_path=latest_BhavCopy()
print("Date of Latest BhavCopy file is: ", data_dates[0])
data_2=pd.read_csv(file_path)

#creating a database with the help of sqlalchemy
engine = create_engine('sqlite:///:memory:')
data_1.to_sql('Equities', engine)
data_2.to_sql("bhavcopy", engine)

#Query 1
print("Query 1 Result")
res1 = pd.read_sql_query('SELECT E."NAME OF COMPANY", B.GAINS from (SELECT ISIN, ((CLOSE-OPEN)/OPEN) AS GAINS FROM bhavcopy) \
      AS B INNER JOIN Equities AS E on B.ISIN=E." ISIN NUMBER" ORDER BY B.GAINS DESC LIMIT 25' , engine)
print(res1)


#Query 2
print("Query 2 Results")
imm_path=os.path.join(path, "Bhavcopies")
index=1
for file in os.listdir(imm_path):
    file_path=os.path.join(imm_path, file)
    data=pd.read_csv(file_path)
    table_name=f"bhavcopy{index}"
    data.to_sql(table_name, engine)
    print("Result", index)
    print("Bhavcopy data is for data:", data_dates[index-1])
    res = pd.read_sql_query(f'SELECT E."NAME OF COMPANY", B.GAINS from (SELECT ISIN, ((CLOSE-OPEN)/OPEN) AS GAINS FROM {table_name}) \
        AS B INNER JOIN Equities AS E on B.ISIN=E." ISIN NUMBER" ORDER BY B.GAINS DESC LIMIT 25' , engine)
    print(res)
    if index!=30:
        sql.execute(f'DROP TABLE {table_name}', engine)
    index+=1


#Query 3
res = pd.read_sql_query(f'SELECT E."NAME OF COMPANY", B.GAINS from (SELECT B1.ISIN, ((B1.CLOSE-B2.OPEN)/B2.OPEN) AS GAINS FROM bhavcopy as B1 \
    ,bhavcopy30 as B2 where B1.ISIN=B2.ISIN) AS B INNER JOIN Equities AS E on B.ISIN=E." ISIN NUMBER" ORDER BY B.GAINS DESC limit 25' , engine)
print(res)