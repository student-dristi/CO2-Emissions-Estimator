import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Title
st.title("CO₂ Emissions Estimator")

# User inputs
engine_size = st.number_input("Engine Size (L)", min_value=0.0, step=0.1)
cylinders = st.number_input("Number of Cylinders", min_value=1, step=1)
fuel_consumption = st.number_input("Fuel Consumption (L/100 km)", min_value=0.0, step=0.1)

# Predict and display
if st.button("Estimate CO₂ Emission"):
    input_data = np.array([[engine_size, cylinders, fuel_consumption]])
    prediction = model.predict(input_data)
    st.success(f"Estimated CO₂ Emission: {prediction[0]:.2f} g/km")
