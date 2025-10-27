# model_training/train_model.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
df = pd.read_csv("../data/students.csv")

# Drop non-numeric columns
X = df.drop(["label_disengaged", "name"], axis=1)
y = df["label_disengaged"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Standardize numeric features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ML model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train_scaled, y_train)

# Create models directory if missing
os.makedirs("../models", exist_ok=True)

# Save model and scaler
joblib.dump(model, "../models/risk_model.pkl")
joblib.dump(scaler, "../models/scaler.pkl")

print("✅ Model training complete!")
print("✅ Saved: models/risk_model.pkl & models/scaler.pkl")

# Optional performance score
score = model.score(X_test_scaled, y_test)
print(f"Model Accuracy: {score:.2f}")
