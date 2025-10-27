import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="Student Engagement Risk Analyzer",
    layout="wide"
)

# ---------------------- THEME SWITCH ----------------------
theme = st.sidebar.radio("Theme Mode:", ["Light", "Dark"])

if theme == "Light":
    bg_color = "#FFEBEE"
    text_color = "#7F0000"
    box_bg = "#FFCDD2"
else:
    bg_color = "#1e1e1e"
    text_color = "#FFCDD2"
    box_bg = "#333333"

# Apply Custom CSS
st.markdown(f"""
<style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .main-title {{
        font-size: 36px !important;
        font-weight: 800 !important;
        color: #B71C1C;
        text-align: center;
    }}
    .metric-box {{
        text-align: center;
        border-radius: 10px;
        padding: 12px;
        background-color: #FFCDD2;
        color: #7F0000;
        border: 2px solid #B71C1C;
        font-weight: 600;
    }}
    .stTabs [role="tab"] {{
        background-color: #FFCDD2;
        color: #7F0000 !important;
        border-radius: 8px;
        margin-right: 5px;
        font-weight: 600;
    }}
    .stTabs [role="tab"][aria-selected="true"] {{
        background-color: #B71C1C !important;
        color: white !important;
    }}
</style>
""", unsafe_allow_html=True)

# ---------------------- HEADER ----------------------
st.markdown("<h1 class='main-title'>Student Engagement Risk Analyzer</h1>", unsafe_allow_html=True)

# ---------------------- TABS ----------------------
tab1, tab2, tab3 = st.tabs(["Overview", "Batch Prediction", "Insights"])

# ---------------------- TAB 1: OVERVIEW ----------------------
with tab1:
    st.subheader("About the System")
    st.write("""
    A smart solution to predict student disengagement early and improve intervention accuracy.
    
    ✅ Upload student performance data  
    ✅ Automatic risk scoring  
    ✅ Visual insights for early action  
    """)

# ---------------------- GLOBAL DATA STORE ----------------------
if "pred_df" not in st.session_state:
    st.session_state.pred_df = None

# ---------------------- TAB 2: BATCH PREDICTION ----------------------
with tab2:
    st.header("Upload CSV for Predictions")

    uploaded_file = st.file_uploader("Upload Student Data CSV")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df.head())

        # Mock Predictions (Replace later with real model)
        df["Engagement_Score"] = np.random.rand(df.shape[0])
        df["Risk_Level"] = df["Engagement_Score"].apply(
            lambda x: "High" if x < 0.3 else "Medium" if x < 0.6 else "Low"
        )
        st.session_state.pred_df = df

        st.subheader("Prediction Results")
        st.dataframe(df)

        # Metrics Summary
        risk_counts = df["Risk_Level"].value_counts()
        col1, col2, col3 = st.columns(3)
        col1.metric("High Risk", risk_counts.get("High", 0))
        col2.metric("Medium Risk", risk_counts.get("Medium", 0))
        col3.metric("Low Risk", risk_counts.get("Low", 0))

        # Download CSV
        st.download_button(
            "Download Predictions CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="student_risk_predictions.csv"
        )
    else:
        st.info("Please upload a file to begin!")

# ---------------------- TAB 3: INSIGHTS ----------------------
with tab3:
    st.header("Analytics & Insights")

    pred_df = st.session_state.pred_df

    if pred_df is not None:

        # Chart 1: Risk Level Distribution
        fig = px.bar(
            pred_df["Risk_Level"].value_counts(),
            title="Risk Level Distribution",
            labels={"value": "Student Count", "index": "Risk Level"},
            color=pred_df["Risk_Level"].value_counts().index
        )
        st.plotly_chart(fig, use_container_width=True)

        # Chart 2: Pie Chart
        fig2 = px.pie(pred_df, names="Risk_Level", title="Risk Category Share")
        st.plotly_chart(fig2, use_container_width=True)

        # Filter Option
        st.subheader("Filter by Risk Level")
        selected_risk = st.selectbox("Select Risk Category", ["All", "High", "Medium", "Low"])
        filtered_df = pred_df if selected_risk == "All" else pred_df[pred_df["Risk_Level"] == selected_risk]
        st.dataframe(filtered_df)

        # Student Detail Viewer
        st.subheader("View Student-Level Details")
        student_list = filtered_df.index.tolist()
        selected_id = st.selectbox("Select a student:", student_list)
        st.table(filtered_df.loc[selected_id])

        # ---------------------- ✅ CHATBOT FEATURE ----------------------
        st.subheader("Dropout Prevention Assistant 🤖")

        category = st.selectbox("What concern would you like help with?", [
            "Low attendance",
            "Low academic performance",
            "Financial issues",
            "Mental well-being concerns",
            "Career confusion"
        ])

        if st.button("Get Advice"):
            responses = {
                "Low attendance": "Try creating a structured routine and join study groups to boost motivation.",
                "Low academic performance": "Refer to online learning platforms like NPTEL, Coursera & take regular practice quizzes.",
                "Financial issues": "Approach student welfare cell to know about scholarships and campus work opportunities.",
                "Mental well-being concerns": "Reach out to the college counselor and adopt stress-reducing activities like sports or art.",
                "Career confusion": "Connect with an academic mentor to plan a path based on strengths and future goals."
            }
            st.success(responses[category])

    else:
        st.warning("No prediction data available. Upload a CSV first!")
