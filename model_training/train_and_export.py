import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
df = pd.read_csv("data/students.csv")

# X = features (from f0 to f9)
feature_cols = [c for c in df.columns if c.startswith("f")]
X = df[feature_cols]
y = df["label_disengaged"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Train
model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train_scaled, y_train)

# Create models folder if missing
os.makedirs("models", exist_ok=True)

# Save model + scaler
joblib.dump(model, "models/risk_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("✅ risk_model.pkl and scaler.pkl saved successfully!")
