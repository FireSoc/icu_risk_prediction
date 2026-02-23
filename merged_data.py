import pandas as pd
import os

data_dir = "raw_csvs/"

def load(filename):
    path = os.path.join(data_dir, filename)
    print(f"Loading {filename}...")
    df = pd.read_csv(path, low_memory=False)
    if "row_id" in df.columns:
        df = df.drop(columns=["row_id"])
    return df

admissions = load('ADMISSIONS.csv')
icustays = load('ICUSTAYS.csv')
patients = load('PATIENTS.csv')
diagnoses_icd = load('DIAGNOSES_ICD.csv')
prescriptions = load('PRESCRIPTIONS.csv')
services = load('SERVICES.csv')

icustays = icustays.sort_values(['subject_id', 'intime'])
icustays['next_intime'] = icustays.groupby('subject_id')['intime'].shift(-1)
icustays['outtime'] = pd.to_datetime(icustays['outtime'])
icustays['next_intime'] = pd.to_datetime(icustays['next_intime'])
icustays['days_to_readmission'] = (icustays['next_intime'] - icustays['outtime']).dt.days
icustays['readmitted_30d'] = (icustays['days_to_readmission'] <= 30).astype(int)

df = icustays.merge(admissions, on=['subject_id', 'hadm_id'], how='left')
df = df.merge(patients, on=['subject_id'], how='left')
df = df.merge(diagnoses_icd, on=['subject_id', 'hadm_id'], how='left')
df = df.merge(prescriptions, on=['subject_id', 'hadm_id'], how='left')
df = df.merge(services, on=['subject_id', 'hadm_id'], how='left')

df.to_csv('combined.csv', index=False)
