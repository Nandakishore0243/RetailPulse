import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="RetailPulse Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# --------------------------------------------------
# Main Dashboard
# --------------------------------------------------
st.title("📊 RetailPulse Dashboard")

st.markdown("""
### AI-Powered Retail Analytics Platform

RetailPulse helps businesses make smarter decisions using Data Science and Machine Learning.

Use the sidebar to explore different modules of the dashboard.
""")

st.markdown("---")

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📈 Forecasting",
        value="Active"
    )

with col2:
    st.metric(
        label="👥 Customer Analytics",
        value="Active"
    )

with col3:
    st.metric(
        label="📦 Inventory",
        value="Active"
    )

with col4:
    st.metric(
        label="🚨 Alerts",
        value="Active"
    )

st.markdown("---")

# --------------------------------------------------
# Module Overview
# --------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.info("""
### 📈 Demand Forecasting

Predict future sales using:

• Prophet Model

• LSTM Model

• Hybrid Forecasting
""")

with col2:
    st.success("""
### 👥 Customer Analytics

Analyze customer behavior using:

• RFM Analysis

• Customer Segmentation

• Churn Prediction
""")

col3, col4 = st.columns(2)

with col3:
    st.warning("""
### 📦 Inventory Optimization

Optimize stock levels using:

• Demand Forecast

• Safety Stock

• Reorder Point Analysis
""")

with col4:
    st.error("""
### 🚨 Alerts & Monitoring

Monitor:

• Churn Risk

• Inventory Risk

• Forecast Trends

• System Status
""")

st.markdown("---")

st.caption(
    "RetailPulse Dashboard"
)