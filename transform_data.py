import pandas as pd

df = pd.read_csv("cleaned_data.csv")

# drop IDs
df = df.drop(columns=["subject_id", "hadm_id", "icustay_id"], errors="ignore")

# categorical columns
categorical_cols = [
    "gender", "insurance", "ethnicity",
    "marital_status", "admission_type"
]

existing_cols = [col for col in categorical_cols if col in df.columns]

df = pd.get_dummies(df, columns=existing_cols)

# fill missing values
df = df.fillna(0)

df.to_csv("ml_ready_data.csv", index=False)