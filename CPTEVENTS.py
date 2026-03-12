'''
This program will clean the CPTEVENTS
'''

import pandas as pd
df = pd.read_csv('CPTEVENTS.csv', low_memory=False)

#Dropping cpt_suffix because it's empty
df = df.drop(columns=['cpt_suffix'])

#Standardizing string columns
str_cols = ['costcenter', 'sectionheader', 'subsectionheader', 'description']
for col in str_cols:
    if col in df.columns:
        df[col] = df[col].str.lower().str.strip()

#Converting the chartdate to datetime
df['chartdate'] = pd.to_datetime(df['chartdate'])

#Dropping duplicates
df = df.drop_duplicates()

#printing out the final cleaned csv
print("Final shape:", df.shape)
print(df.head())

#making a new cleaned csv file
df.to_csv('CPTEVENTS_cleaned.csv', index=False)