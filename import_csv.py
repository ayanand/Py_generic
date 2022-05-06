import pyodbc
import sqlalchemy
import pandas as pd
from datetime import datetime

DRIVER     = "ODBC Driver 17 for SQL Server"
USERNAME   = ""
PSSWD      = ""
SERVERNAME = ""
DB         = ""

print(datetime.now());
engine = sqlalchemy.create_engine(
    f"mssql+pyodbc://{USERNAME}:{PSSWD}@{SERVERNAME}/{DB}?driver={DRIVER}", fast_executemany=True
)
conn = engine.connect();
fn="GE2022_Address_Register_20220502_0605.dat";
df = pd.read_csv("C:\\Users\\Ayush.Anand\\Documents\\tmp\\DAT\\"+fn,sep="\t",low_memory=False);
df['filename']=fn;
table = fn.split('.')[0];
df.head(10).to_sql(table, con=conn, index=False,chunksize=10000,schema="dbo", if_exists='replace')
print(datetime.now());
