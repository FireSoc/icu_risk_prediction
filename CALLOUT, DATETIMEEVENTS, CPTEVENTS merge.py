'''

This python program will merge the  CALLOUT, DATETIMEEVENTS, CPTEVENTS csvs

'''

import pandas as pd

#importing the cleaned csvs
df_CALLOUT = pd.read_csv('CALLOUT_cleaned.csv', low_memory=False)
df_DATETIMEEVENTS = pd.read_csv('DATETIMEEVENTS_cleaned.csv', low_memory=False)
df_CPTEVENTS = pd.read_csv('CPTEVENTS_cleaned.csv', low_memory=False)

#finding out how many patients appear in the subject_id column (this is a test)
# print(len(set(df_CALLOUT['subject_id']) & set(df_CPTEVENTS['subject_id'])))
# print(len(set(df_CALLOUT['subject_id']) & set(df_DATETIMEEVENTS['subject_id'])))
# print(len(set(df_CPTEVENTS['subject_id']) & set(df_DATETIMEEVENTS['subject_id'])))

#Merging them csvs
df_merged_part_one = pd.merge(df_CALLOUT, df_DATETIMEEVENTS, on='subject_id', how='inner')


df_merged_part_two = pd.merge(df_merged_part_one,df_CPTEVENTS, on='subject_id', how='inner')

#dropping duplicates(just in case)
df_merged_part_two = df_merged_part_two.drop_duplicates(subset='subject_id', keep='last')

#Drppping nulls (Just in case)
print(df_merged_part_two.isnull().sum())

print(df_merged_part_two)
print(df_merged_part_two.shape)
print(df_merged_part_two.columns.tolist())

#making a new csv with the merged data
df_merged_part_two.to_csv('CALLOUTDATETIMEEVENTSCPTEVENTSMERGED_cleaned.csv', index=False)