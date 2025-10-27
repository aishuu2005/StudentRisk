# model_training/inference.py

import joblib
import numpy as np

# Load saved model & scaler
model = joblib.load("../models/risk_model.pkl")
scaler = joblib.load("../models/scaler.pkl")

def predict_risk(input_data):
    # input_data must be a list of feature values in correct order
    scaled = scaler.transform([input_data])
    prediction = model.predict(scaled)
    probability = model.predict_proba(scaled)[0][1]
    return prediction[0], probability
