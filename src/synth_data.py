# src/synth_data.py
import numpy as np
import pandas as pd
import os

os.makedirs("data", exist_ok=True)
n = 1200
np.random.seed(42)

df = pd.DataFrame({
  "id": np.arange(1, n+1),
  "name": ["Student_"+str(i) for i in range(1,n+1)],
  "gender": np.random.choice(["M","F","O"], size=n, p=[0.5,0.48,0.02]),
  "age": np.random.randint(17, 26, size=n),
  "year_of_study": np.random.choice([1,2,3,4], size=n, p=[0.25,0.25,0.25,0.25]),
  "parent_income": np.random.choice([15000,30000,60000,100000], size=n, p=[0.4,0.3,0.2,0.1]),
  "has_part_time_job": np.random.binomial(1, 0.18, size=n),
  "attendance_percent": np.clip(np.random.normal(78,12,n), 30,100),
  "classes_missed_last_month": np.clip(np.random.poisson(3, n), 0, 30),
  "avg_internal_marks": np.clip(np.random.normal(62,14,n), 20,100),
  "last_semester_cgpa": np.round(np.clip(np.random.normal(6.5,1.2,n), 0,10),2),
  "assignment_submission_rate": np.clip(np.random.beta(5,1.5,n)*100, 0,100),
  "lab_attendance_percent": np.clip(np.random.normal(80,10,n), 20,100),
  "counseling_visits_last_6_months": np.random.poisson(0.4, n),
  "mentor_sessions_attended": np.random.poisson(0.8, n),
  "weekly_study_hours": np.clip(np.random.normal(12,6,n), 0,70),
  "stress_survey_score": np.clip(np.random.normal(4.2,2.1,n), 0,10),
  "engagement_lms_count": np.clip(np.random.poisson(25, n), 0,300),
  "internet_reliability_score": np.random.choice([1,2,3,4,5], size=n, p=[0.05,0.1,0.3,0.4,0.15]),
  "financial_issue_flag": np.random.binomial(1, 0.15, size=n)
})

# synthetic label rule
df["label_disengaged"] = (
    ((df.attendance_percent < 65) & (df.weekly_study_hours < 8))
    | (df.avg_internal_marks < 45)
).astype(int)

df.to_csv("data/students.csv", index=False)
print("Saved data/students.csv —", len(df), "rows")
