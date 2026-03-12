'''
This program will clean the DATETIMEEVENTS program

'''

import pandas as pd

df = pd.read_csv('DATETIMEEVENTS.csv', low_memory=False)

#Dropping the empty columns
df = df.drop(columns=['resultstatus','stopped', 'warning', "error"], errors='ignore')

# Dropping the null rows
df = df.dropna(subset=['value', 'icustay_id'])

#Timestamps
df['charttime'] = pd.to_datetime(df['charttime'])
df['storetime'] = pd.to_datetime(df['storetime'])

#String columns (turning them into lowercase)

df['valueuom'] = df['valueuom'].str.lower().str.strip()
df['value'] = df['value'].str.lower().str.strip()

#Printing out the new CSV
print(df.shape)
print(df.head())


#Saving it as a new CSV
df.to_csv('DATETIMEEVENTS_cleaned.csv', index=False)