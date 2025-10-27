# Student Engagement Risk — Hackathon MVP

## Purpose
Predict student disengagement and provide early interventions.

## Repo layout
- data/       : raw and processed CSVs
- src/        : preprocessing, training, inference scripts
- notebooks/  : EDA and experiments
- models/     : saved model artifacts (.joblib/.pkl)
- app/        : Streamlit dashboard
- docs/       : slides, demo notes

## Quick start
1. Create venv and install requirements: `python -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
2. Run `python src/synth_data.py` if no dataset present (creates data/students.csv)
3. Train baseline: `python src/train.py`
4. Launch dashboard: `streamlit run app/app.py`

## Team roles (example)
- Data & Feature Engineer: produce cleaned CSV
- Modeler: train and evaluate ML models
- Frontend: build Streamlit app and demo flow
