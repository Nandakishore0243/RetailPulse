import streamlit as st
import pandas as pd

st.title("👥 Customer Analytics Dashboard")

segment_df = pd.read_csv(
    "data/processed/customer_segments.csv"
)

churn_df = pd.read_csv(
    "data/processed/churn_predictions.csv"
)
st.subheader("Customer Segments")

st.dataframe(segment_df.head(20))
segment_counts = (
    segment_df["Segment"]
    .value_counts()
)

st.subheader("Segment Distribution")

st.bar_chart(segment_counts)
st.subheader("Churn Risk Distribution")

churn_counts = (
    churn_df["Predicted"]
    .value_counts()
)

st.bar_chart(churn_counts)
st.subheader("Key Metrics")

col1,col2,col3 = st.columns(3)

col1.metric(
    "Total Customers",
    len(segment_df)
)

col2.metric(
    "At Risk",
    segment_counts.get(
        "At-Risk",
        0
    )
)

col3.metric(
    "Predicted Churn",
    churn_counts.get(
        1,
        0
    )
)
st.subheader(
    "High Risk Customers"
)

high_risk = churn_df[
    churn_df["Predicted"] == 1
]

st.dataframe(
    high_risk.head(20)
)
with open(
    "../reports/customer_report.csv",
    "rb"
) as file:

    st.download_button(
        label="📥 Download Customer CSV",
        data=file,
        file_name="customer_report.csv",
        mime="text/csv"
    )