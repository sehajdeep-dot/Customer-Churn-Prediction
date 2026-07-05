import streamlit as st 
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD MODEL ---------------- #

model = joblib.load("models/customer_churn_pipeline.pkl")

# ---------------- CUSTOM CSS ---------------- #

# ---------------- PREMIUM CSS ---------------- #

st.markdown("""
<style>

.stApp{
    background:#0B1120;
}

.block-container{
    padding-top:2rem;
    padding-left:3rem;
    padding-right:3rem;
}

.main-title{
    font-size:48px;
    font-weight:800;
    color:white;
    letter-spacing:.5px;
}

.subtitle{
    font-size:18px;
    color:#94A3B8;
    margin-bottom:25px;
}

/* KPI Cards */

.card{

    background:linear-gradient(145deg,#182235,#101827);

    border:1px solid #263548;

    border-radius:18px;

    padding:25px;

    transition:.35s;

    box-shadow:0px 8px 20px rgba(0,0,0,.35);

    text-align:center;

}

.card:hover{

    transform:translateY(-6px);

    border:1px solid #3B82F6;

    box-shadow:0px 10px 28px rgba(59,130,246,.25);

}

.card h4{

    color:#94A3B8;

    margin-bottom:10px;

}

.card h2{

    color:white;

    font-size:36px;

}

/* Sidebar */

section[data-testid="stSidebar"]{

    background:#101827;

    border-right:1px solid #1E293B;

}

section[data-testid="stSidebar"] *{

    color:white;

}

/* Button */

.stButton>button{

    width:100%;

    height:58px;

    border:none;

    border-radius:14px;

    font-size:20px;

    font-weight:700;

    color:white;

    background:linear-gradient(90deg,#2563EB,#7C3AED);

    transition:.3s;

}

.stButton>button:hover{

    transform:translateY(-3px);

    box-shadow:0px 0px 18px rgba(59,130,246,.45);

}

/* Inputs */

.stSelectbox>div>div{

    background:#182235;

    border-radius:10px;

}

.stNumberInput>div>div>input{

    background:#182235;

    border-radius:10px;

}

.stTextInput>div>div>input{

    background:#182235;

}

.stSlider{

    padding-top:8px;

}

/* Metric */

div[data-testid="stMetric"]{

    background:#182235;

    border-radius:15px;

    padding:20px;

    border:1px solid #263548;

}

/* Tables */

[data-testid="stDataFrame"]{

    border-radius:15px;

    overflow:hidden;

}

/* Scroll */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#334155;

    border-radius:20px;

}

hr{

    border:1px solid #263548;

}

</style>

""",unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("📊 Navigation")

    page = st.radio(
        "Go To",
        [
            "Prediction",
            "Analytics",
            "About"
        ]
    )

    st.write("---")

    st.info("Customer Churn Prediction using Random Forest Pipeline")

# ---------------- HEADER ---------------- #

st.markdown(
"""
<div class='main-title'>
📊 Customer Churn Prediction Dashboard
</div>

<div class='subtitle'>
AI Powered Customer Retention Analytics using Random Forest Pipeline
</div>
""",
unsafe_allow_html=True
)

st.write("")

# ---------------- KPI CARDS ---------------- #

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown("""
<div class='card'>
<h4>🤖 Model</h4>
<h2>Random Forest</h2>
<p style="color:#60A5FA;">Pipeline Based</p>
</div>
""",unsafe_allow_html=True)

with c2:

    st.markdown("""
<div class='card'>
<h4>📂 Dataset</h4>
<h2>7043</h2>
<p style="color:#22C55E;">Customers</p>
</div>
""", unsafe_allow_html=True)

with c3:

    st.markdown("""
<div class='card'>
<h4>Features</h4>
<h2>19</h2>
</div>
""",unsafe_allow_html=True)

with c4:

    st.markdown("""
<div class='card'>
<h4>Target</h4>
<h2>Churn</h2>
</div>
""",unsafe_allow_html=True)

st.write("")
# ================= CUSTOMER INFORMATION ================= #

st.header("👤 Customer Information")

left, right = st.columns(2)

with left:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        ["No", "Yes"]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

with right:

    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=800.0
    )

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes","No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["No","Yes","No phone service"]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        ["Yes","No"]
    )
    # ================= INTERNET SERVICES ================= #

st.header("🌐 Internet Services")

left2, right2 = st.columns(2)

with left2:

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL","Fiber optic","No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes","No","No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes","No","No internet service"]
    )

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes","No","No internet service"]
    )

with right2:

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes","No","No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes","No","No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes","No","No internet service"]
    )
    

    # ================= BILLING ================= #

st.header("💳 Contract & Billing")

left3,right3 = st.columns(2)

with left3:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

with right3:

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )
    # ================= PREDICTION ================= #

st.write("")
st.write("")

predict = st.button(
    "🔮 Predict Customer Churn",
    use_container_width=True
)

if predict:

    input_df = pd.DataFrame({

        "gender":[gender],
        "SeniorCitizen":[1 if senior=="Yes" else 0],
        "Partner":[partner],
        "Dependents":[dependents],
        "tenure":[tenure],
        "PhoneService":[phone_service],
        "MultipleLines":[multiple_lines],
        "InternetService":[internet_service],
        "OnlineSecurity":[online_security],
        "OnlineBackup":[online_backup],
        "DeviceProtection":[device_protection],
        "TechSupport":[tech_support],
        "StreamingTV":[streaming_tv],
        "StreamingMovies":[streaming_movies],
        "Contract":[contract],
        "PaperlessBilling":[paperless],
        "PaymentMethod":[payment_method],
        "MonthlyCharges":[monthly],
        "TotalCharges":[total]

    })

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.write("---")

    if prediction == "Yes" or prediction == 1:

        st.error("🚨 Customer is likely to Churn")

    else:

        st.success("✅ Customer is likely to Stay")
        st.write("### 📊 Churn Probability")


    # ================= RESULT SECTION ================= #

if predict:

    st.write("")
    st.write("---")
    st.subheader("📊 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:

        if prediction == "Yes" or prediction == 1:

            st.error("🚨 Customer is likely to Churn")

        else:

            st.success("✅ Customer is likely to Stay")
            Sst.write("### 📊 Churn Probability")

    progress_value = max(0.0, min(1.0, float(probability)))
    st.progress(progress_value)

    st.write(f"**Probability : {probability*100:.2f}%**")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability*100,
        title={"text": "Churn Probability (%)"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#3B82F6"},
            "steps": [
                {"range": [0, 35], "color": "#22C55E"},
                {"range": [35, 70], "color": "#F59E0B"},
                {"range": [70, 100], "color": "#EF4444"}
            ]
        }
    ))

    fig.update_layout(
        template="plotly_dark",
        height=350
    )

    st.plotly_chart(fig, use_container_width=True)

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    st.metric(
            "Churn Probability",
            f"{probability*100:.2f}%"
        )

    st.progress(float(probability))


    with col2:

        summary = pd.DataFrame({

            "Feature":[
                "Gender",
                "Senior Citizen",
                "Partner",
                "Dependents",
                "Tenure",
                "Monthly Charges",
                "Total Charges",
                "Contract",
                "Internet Service"
            ],

            "Value":[
                gender,
                senior,
                partner,
                dependents,
                tenure,
                monthly,
                total,
                contract,
                internet_service
            ]

        })

        st.dataframe(
            summary,
            use_container_width=True
        )
        # ================= ANALYTICS PAGE ================= #

if page == "Analytics":

    st.title("📈 Analytics Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Customers", "7043")

    with col2:
        st.metric("Model", "Random Forest")

    with col3:
        st.metric("Features", "19")

    st.write("---")

    # Figure create karna zaroori hai
    fig = go.Figure()

    fig.add_bar(
        x=["Logistic Regression", "Decision Tree", "Random Forest"],
        y=[78.75, 72.64, 78.75],
        marker_color=["#3B82F6", "#F97316", "#8B5CF6"]
    )

    fig.update_layout(
        title="Model Accuracy Comparison",
        template="plotly_dark",
        xaxis_title="Models",
        yaxis_title="Accuracy (%)",
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("Random Forest performed better than Decision Tree and was selected as the final model.")
    # ================= ABOUT PAGE ================= #

if page == "About":

    st.title("ℹ️ About Project")

    st.markdown("""
### Customer Churn Prediction System

This project predicts whether a telecom customer is likely to leave the company using Machine Learning.

### Project Workflow

- Data Collection
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Model Building
- Pipeline Creation
- Streamlit Deployment

### Dataset

- Telco Customer Churn Dataset
- Total Records : 7043
- Features : 19
- Target Variable : Churn

### Machine Learning Models

- Logistic Regression
- Decision Tree
- Random Forest

### Final Model

Random Forest Pipeline

### Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Plotly
- Joblib
""")