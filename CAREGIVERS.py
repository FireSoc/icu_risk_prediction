'''
This program will clean the CAREGIVERS csv file
'''

import pandas as pd

df = pd.read_csv('CAREGIVERS.csv', low_memory=False)

# Dropping the rows
df = df.dropna(subset=['label'])

# Standardizing string columns
for col in ['label', 'description']:
    df[col] = df[col].str.lower().str.strip()

#printing out the final product
print("Final shape:", df.shape)
print(df.head())

#creates the newly cleaned CSV
df.to_csv('CAREGIVERS_cleaned.csv', index=False)