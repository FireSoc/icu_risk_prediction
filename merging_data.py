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
labevents = load("LABEVENTS.csv")
transfers = load("TRANSFERS.csv")
procedures_icd = load("PROCEDURES_ICD.csv")

# grouping by hadm_id
diagnoses_agg = diagnoses_icd.groupby(['subject_id', 'hadm_id']).agg(
    icd9_codes=('icd9_code', list),
    diagnosis_count=('icd9_code', 'count')
    ).reset_index()

prescriptions_agg = prescriptions.groupby(['subject_id', 'hadm_id', 'icustay_id']).agg(
    drugs=('drug', list),
    prescription_count=('drug', 'count')
).reset_index()

services_agg = services.groupby(['subject_id', 'hadm_id']).agg(
    services=('curr_service', list)
).reset_index()



labs_agg = labevents.groupby(["subject_id", "hadm_id"]).agg(
    lab_count=("itemid", "count"),
    abnormal_lab_count=("flag", lambda x: x.notna().sum())
).reset_index()

transfers_agg = transfers.groupby(["subject_id", "hadm_id"]).size().reset_index(name="transfer_count")

procedures_agg = procedures_icd.groupby(["subject_id", "hadm_id"]).agg(
    procedure_count=("icd9_code", "count")
).reset_index()


# merging
df = icustays.merge(admissions, on=['subject_id', 'hadm_id'], how='left')
df = df.merge(patients, on=['subject_id'], how='left')
df = df.merge(diagnoses_agg, on=['subject_id', 'hadm_id'], how='left')
df = df.merge(prescriptions_agg, on=['subject_id', 'hadm_id', 'icustay_id'], how='left')
df = df.merge(services_agg, on=['subject_id', 'hadm_id'], how='left')

df = df.merge(labs_agg, on=["subject_id", "hadm_id"], how="left")
df = df.merge(transfers_agg, on=["subject_id", "hadm_id"], how="left")
df = df.merge(procedures_agg, on=["subject_id", "hadm_id"], how="left")

for col in ["lab_count", "abnormal_lab_count", "transfer_count", "procedure_count"]:
    df[col] = df[col].fillna(0)

df.to_csv('merged.csv', index=False)
