import streamlit as st
import joblib
import numpy as np

model = joblib.load("asteroid_model.pkl")

st.title("NEO Sentinel")

absolute_magnitude = st.number_input("Absolute Magnitude")

diameter_min = st.number_input("Diameter Min")

diameter_max = st.number_input("Diameter Max")

velocity = st.number_input("Relative Velocity")

miss_distance = st.number_input("Miss Distance")

if st.button("Predict"):

    data = np.array([
        [
            absolute_magnitude,
            diameter_min,
            diameter_max,
            velocity,
            miss_distance
        ]
    ])

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error(" Hazardous Asteroid")
    else:
        st.success("Safe Asteroid")


        """
        Absolute Magnitude: 22.1
Diameter Min: 95
Diameter Max: 210
Relative Velocity: 42350
Miss Distance: 1800000

        """