import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📦 Inventory Optimization Dashboard")

st.write("""
This page displays inventory recommendations generated from
inventory optimization analysis.
""")

# Load Data
inventory_df = pd.read_csv(
    "../data/processed/inventory_optimization.csv"
)

# -------------------------
# Inventory Data
# -------------------------
st.subheader("Inventory Recommendations")

st.dataframe(
    inventory_df.head(20),
    use_container_width=True
)

# -------------------------
# Inventory Status Chart
# -------------------------
st.subheader("Inventory Status Distribution")

status_counts = (
    inventory_df["Inventory_Status"]
    .value_counts()
    .reset_index()
)

status_counts.columns = [
    "Inventory Status",
    "Count"
]

fig = px.bar(
    status_counts,
    x="Inventory Status",
    y="Count",
    title="Inventory Status Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -------------------------
# Key Metrics
# -------------------------
st.subheader("Key Metrics")

reorder_count = (
    inventory_df["Inventory_Status"]
    == "Reorder Required"
).sum()

sufficient_count = (
    inventory_df["Inventory_Status"]
    == "Stock Sufficient"
).sum()

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Reorder Required",
        reorder_count
    )

with col2:
    st.metric(
        "Stock Sufficient",
        sufficient_count
    )

# -------------------------
# Reorder Products
# -------------------------
st.subheader("Products Needing Reorder")

reorder_df = inventory_df[
    inventory_df["Inventory_Status"]
    == "Reorder Required"
]

st.dataframe(
    reorder_df.head(20),
    use_container_width=True
)

# -------------------------
# Summary
# -------------------------
st.success(
    f"{reorder_count} products require replenishment."
)
with open(
    "../reports/inventory_report.csv",
    "rb"
) as file:

    st.download_button(
        label="📥 Download Inventory CSV",
        data=file,
        file_name="inventory_report.csv",
        mime="text/csv"
    )