# Dataset Plan

## Columns (mandatory)
id, name, gender, age, year_of_study, program,
parent_income, scholarship_flag, has_part_time_job,
attendance_percent, classes_missed_last_month, avg_internal_marks,
last_semester_cgpa, assignment_submission_rate, lab_attendance_percent,
counseling_visits_last_6_months, mentor_sessions_attended,
weekly_study_hours, stress_survey_score, engagement_lms_count,
internet_reliability_score, financial_issue_flag, label_disengaged

## Label definition (for demo)
label_disengaged = 1 if any of:
- attendance_percent < 65 and weekly_study_hours < 8
- avg_internal_marks < 45
- last_semester_cgpa dropped by > 0.5 from previous semester

If real labels are available from the institution, use them instead.

## Data sources
- College attendance logs (CSV)
- Internal assessment marks (CSV)
- LMS engagement exports (CSV)
- Counseling records (anonymized)
- Student survey (stress, internet reliability)
