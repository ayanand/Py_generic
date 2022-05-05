import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'regiccsmi.76755b4f90dd.database.windows.net' 
database = 'stg' 
username = 'regbcp' 
password = 'regbcp' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute('SELECT 1')

for i in cursor:
    print(i)
