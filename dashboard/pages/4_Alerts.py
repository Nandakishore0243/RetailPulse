import streamlit as st
import pandas as pd

st.title("🚨 Alerts & Monitoring Dashboard")

st.write("""
This page monitors key business metrics and generates alerts.
""")

# Load datasets
forecast_df = pd.read_csv("data/processed/hybrid_forecast.csv")
customer_df = pd.read_csv("data/processed/customer_segments.csv")
inventory_df = pd.read_csv("data/processed/inventory_optimization.csv")

# --------------------------------------------------
# Demand Monitoring
# --------------------------------------------------

avg_forecast = forecast_df["Hybrid"].mean()

st.subheader("Demand Monitoring")

st.metric(
    label="Average Forecast Demand",
    value=f"{avg_forecast:,.2f}"
)

if avg_forecast > 25000:
    st.error("⚠️ ALERT: High Demand Expected")
else:
    st.success("✅ Demand Levels Normal")

# --------------------------------------------------
# Churn Monitoring
# --------------------------------------------------

predicted_churn = int(len(customer_df) * 0.10)

st.subheader("Customer Churn Monitoring")

st.metric(
    label="Predicted Churn Customers",
    value=predicted_churn
)

if predicted_churn > 500:
    st.warning("⚠️ High Customer Churn Risk")
else:
    st.success("✅ Churn Levels Acceptable")

# --------------------------------------------------
# Inventory Monitoring
# --------------------------------------------------

reorder_count = (
    inventory_df["Current_Stock"]
    < inventory_df["Reorder_Point"]
).sum()

st.subheader("Inventory Monitoring")

st.metric(
    label="Products Needing Reorder",
    value=reorder_count
)

if reorder_count > 50:
    st.error("⚠️ Inventory Replenishment Required")
else:
    st.success("✅ Inventory Status Healthy")

# --------------------------------------------------
# Overall Status
# --------------------------------------------------

st.subheader("Overall System Status")

if (
    avg_forecast > 25000
    or predicted_churn > 500
    or reorder_count > 50
):
    st.error("🔴 Action Required")
else:
    st.success("🟢 All Systems Normal")