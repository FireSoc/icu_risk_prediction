'''
This python program will clean the D_LABITEMS csv file
'''

import pandas as pd

df = pd.read_csv('D_LABITEMS.csv', low_memory=False)

#Dropping the null rows
df = df.dropna(subset=["loinc_code"])

#Standarziing string columns (lowercasing the words)
str_cols=  ["fluid", "category", "label"]

for col in str_cols:
    df[col] = df[col].str.strip().str.lower()

#printing out the newly cleaned csv

print("Final shape:", df.shape)
print(df.head())

#Making a new CSV

df.to_csv("D_LABITEMS_cleaned.csv", index=False)