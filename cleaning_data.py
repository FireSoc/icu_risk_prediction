import pandas as pd

df = pd.read_csv('merged.csv', low_memory=False)
df.dropna()
df.drop_duplicates()

str_cols = [
    'admission_type', 'admission_location', 'discharge_location',
    'insurance', 'language', 'religion', 'marital_status', 'ethnicity',
    'diagnosis', 'first_careunit', 'last_careunit', 'dbsource', 'gender'
]
for col in str_cols:
    if col in df.columns:
        df[col] = df[col].str.lower().str.strip()

drop_cols = [
    'dob', 'dod', 'dod_hosp', 'dod_ssn',
    'edregtime', 'edouttime',
    'has_chartevents_data'
]
df = df.drop(columns=[col for cols in drop_cols])

df = df.dropna(subset=['subject_id', 'hadm_id', 'icustay_id'])
df = df[df['los'] > 0]

df.to_csv('cleaned_data.csv', index=False)