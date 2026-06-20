import streamlit as st
import pandas as pd

st.title("📈 Demand Forecasting Dashboard")

st.write("""
This page displays demand forecasting results generated
using Prophet, LSTM, and Hybrid models.
""")

sales_df = pd.read_csv(
    "../data/processed/sales_forecast.csv"
)

lstm_df = pd.read_csv(
    "../data/processed/lstm_forecast.csv"
)

hybrid_df = pd.read_csv(
    "../data/processed/hybrid_forecast.csv"
)

st.subheader("Hybrid Forecast Data")

st.dataframe(
    hybrid_df.head(10)
)
st.subheader("Forecast Comparison")

st.line_chart(
    hybrid_df[["Actual", "Prophet", "LSTM", "Hybrid"]]
)
st.subheader("Forecast Accuracy")

mae_data = {
    "Model": ["Prophet", "LSTM", "Hybrid"],
    "MAE": [20253.37, 14078.19, 16030.93]
}

mae_df = pd.DataFrame(mae_data)

st.bar_chart(
    mae_df.set_index("Model")
)
st.subheader("What-If Analysis")

growth = st.slider(
    "Expected Demand Increase (%)",
    min_value=0,
    max_value=100,
    value=10
)

latest_forecast = hybrid_df["Hybrid"].iloc[-1]

adjusted_forecast = latest_forecast * (1 + growth/100)

st.metric(
    "Adjusted Forecast Demand",
    f"{adjusted_forecast:,.2f}"
)
with open(
    "../reports/forecast_report.csv",
    "rb"
) as file:

    st.download_button(
        label="📥 Download Forecast CSV",
        data=file,
        file_name="forecast_report.csv",
        mime="text/csv"
    )