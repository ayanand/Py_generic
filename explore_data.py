import pandas as pd
import re

fn="GE2022_Elector_List_20220502_0605.dat";
df = pd.read_csv("C:\\Users\\Ayush.Anand\\Documents\\tmp\\DAT\\"+fn,sep="\t",low_memory=False);
print(pd.io.sql.get_schema(df.reset_index(), 'data'));
df =df.astype('str')
print('create table ',fn,'    (')
for (columnName, columnData) in df.iteritems():
    print(re.sub(r'(?<!^)(?=[A-Z])', '_', columnName).lower()," nvarchar (",df[columnName].str.len().max()+1,") ,")
    #print('Column Name : ', columnName);
    #print('Max length ',df[columnName].str.len().max());
    
    #if columnData.dtype == 'object':
     #   print('Max length ',df[columnName].str.len().max());
    #print('Column Contents : ', columnData.values);
    #print('Column Contents : ', columnData.dtype);
    #print('Column Contents : ', columnData.shape);
    #print('Column Contents : ', columnData.infer_objects().dtype);
print(');')
    
    
