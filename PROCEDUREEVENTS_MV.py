'''
This program will clean the PROCEDUREEVENTS_MV csv
'''

import pandas as pd

df = pd.read_csv('PROCEDUREEVENTS_MV.csv', low_memory=False)

#Dropping the empty columns and rows
df = df.drop(columns=['secondaryordercategoryname', 'location', 'locationcategory','comments_date','comments_editedby','comments_canceledby'])

#timestamps
df['starttime'] = pd.to_datetime(df['starttime'])
df['endtime'] = pd.to_datetime(df['endtime'])
df['storetime'] = pd.to_datetime(df['storetime'])

#String columns (turning them into lowercase using a for loop)
str_cols = ['valueuom', 'ordercategorydescription', 'statusdescription', 'ordercategoryname']
for col in str_cols:
    df[col] = df[col].str.lower().str.strip()

#Printing the newly cleaned csv
print(df.head())
print("")
print(df.shape)
print("")
print(df.columns.tolist())
#newly cleaned csv
df.to_csv('PROCEDUREEVENTS_MV_cleaned.csv', index=False)