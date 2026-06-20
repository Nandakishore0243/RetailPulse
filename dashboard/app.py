import streamlit as st

st.set_page_config(
    page_title="RetailPulse Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 RetailPulse Dashboard")

st.markdown("""
Welcome to RetailPulse Analytics Platform.

Use the sidebar to navigate between:
- Forecasting
- Customer Analytics
- Inventory Optimization
- Alerts & Monitoring
""")