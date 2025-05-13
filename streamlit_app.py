import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load trained model
model = joblib.load("xgb_timeseries_model.pkl")

st.title("📦 Oraimo Sales Forecasting App")
st.write("Forecast future sales based on past performance.")

# Input UI for features
day = st.number_input("Day of the month", min_value=1, max_value=31, value=1)
month = st.number_input("Month (1-12)", min_value=1, max_value=12, value=10)
weekday = st.number_input("Day of the week (0-6, Monday=0)", min_value=0, max_value=6, value=0)
week = st.number_input("Week of the year", min_value=1, max_value=53, value=40)
is_weekend = st.selectbox("Is it a weekend?", [0, 1], index=0)
is_holiday = st.selectbox("Is it a holiday?", [0, 1], index=0)
lag_1 = st.number_input("Sales 1 day ago (lag_1)", value=0.0)
lag_7 = st.number_input("Sales 7 days ago (lag_7)", value=0.0)
lag_14 = st.number_input("Sales 14 days ago (lag_14)", value=0.0)
rolling_mean_7 = st.number_input("7-day rolling mean", value=0.0)
rolling_std_7 = st.number_input("7-day rolling std", value=0.0)


# Predict button
if st.button("Forecast Sales"):
    input_data = np.array([[day, month, weekday, week, is_weekend, is_holiday, lag_1, lag_7, lag_14, rolling_mean_7, rolling_std_7]])
    prediction = model.predict(input_data)[0]
    st.success(f"📈 Forecasted Sales: **{prediction:.2f} units**")
