# model_training/clean_data.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

# Load dataset
df = pd.read_csv("data/students.csv")

# Drop duplicates
df.drop_duplicates(inplace=True)

# Handle missing values (if any)
for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].median(), inplace=True)

# Outlier handling for numeric columns
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns

for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    df[col] = np.clip(df[col], lower, upper)

# Encode categorical columns
df = pd.get_dummies(df, columns=["gender"], drop_first=True)

# Save cleaned dataset
os.makedirs("data/processed", exist_ok=True)
df.to_csv("data/processed/cleaned_students.csv", index=False)

print("Cleaning completed successfully!")
print("Saved cleaned file: data/processed/cleaned_students.csv")
print("Final shape:", df.shape)
