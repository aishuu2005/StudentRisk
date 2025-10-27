Student Engagement Risk Analyzer

Early Intervention System for Academic Success

Team Details

Team Name: TrinityX
Team Members:
• Aishwarya S – 23bca122@caias.in
• Tejaswini Purushottam Kumbhar – 23bca047@caias.in

Overview

This project delivers a practical solution to help institutions identify students who may be at risk of low academic engagement. The system uses key performance indicators to generate a risk score and presents the results through a clean and interactive dashboard. It enables faculty to take proactive steps and provide timely support.

Our focus is simplicity, speed, and immediate real-world usefulness.

Solution Highlights

• Automated risk score prediction for individual and batch student records
• Clear classification into High, Medium, and Low risk groups
• Interactive analytics dashboard for faculty decision support
• Scalable design that can fit into existing academic systems
• Built in under 8 hours with an optimized MVP approach

Technical Workflow

Input student data through form or CSV upload

Data preprocessing using stored scaler

Machine learning model generates risk probability

Risk class and insights displayed in dashboard

Machine Learning Artifacts:
• risk_model.pkl
• scaler.pkl

Instructions to Run the Project
1. Clone the repository
git clone https://github.com/your-repo/student-risk-analyzer.git
cd student-risk-analyzer

2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate     # for Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the Streamlit Dashboard
cd streamlit_app
streamlit run app.py

5. View in browser
Streamlit will display a URL like:
http://localhost:8501
Open it to interact with the dashboard.

Tech Stack
| Category              | Tools                       |
| --------------------- | --------------------------- |
| Programming           | Python                      |
| Data & ML             | Pandas, NumPy, Scikit-Learn |
| Visualization         | Plotly, Matplotlib          |
| Dashboard             | Streamlit                   |
| Version Control       | Git, GitHub                 |
| Optional Enhancements | FastAPI, Flask, SHAP        |

Deliverables
| Component                           | Status      |
| ----------------------------------- | ----------- |
| Synthetic dataset and preprocessing | Completed   |
| Risk prediction model               | Completed   |
| Streamlit analytics dashboard       | Completed   |
| Batch upload support                | Completed   |
| Workflow documentation              | Completed   |
| Explainability features             | In progress |

Future Scope

• Explainable AI modules to interpret risk drivers
• API integration for institution-wide access
• Automated alerts and follow-ups to mentors
• Long-term engagement tracking dashboards
• Personalized student recommendations
