import pyodbc
import sqlalchemy
import pandas as pd
from datetime import datetime

DRIVER     = "ODBC Driver 17 for SQL Server"
USERNAME   = "regbcp"
PSSWD      = "regbcp"
SERVERNAME = "regiccsmi.76755b4f90dd.database.windows.net"
DB         = "STG"

print(datetime.now());
engine = sqlalchemy.create_engine(
    f"mssql+pyodbc://{USERNAME}:{PSSWD}@{SERVERNAME}/{DB}?driver={DRIVER}", fast_executemany=True
)
conn = engine.connect();
fn="GE2022_Address_Register_20220502_0605.dat";
df = pd.read_csv("C:\\Users\\Ayush.Anand\\OneDrive - electionson\\Documents\\tmp\\GE2022_TiP_Extracts_20220502_0605\\DAT\\"+fn,sep="\t",low_memory=False);
df['filename']=fn;
table = fn.split('.')[0];
df.head(10).to_sql(table, con=conn, index=False,chunksize=10000,schema="dbo", if_exists='replace')
print(datetime.now());
