import joblib
import numpy as np
import streamlit as st
import pandas as pd


# Load the saved model
with open('Kneighbors_classifier_model.pkl', 'rb') as file:
    model = joblib.load(file)

# Heading and description
st.markdown("<h1 style='color:purple;'>Excercise Angles</h1>", unsafe_allow_html=True)
st.write("""
This application predicts the excercise  based on angles.
""")


# Input grid
col1, col2, col3 = st.columns(3)

with col1:
    Shoulder_Angle = st.number_input("Shoulder_Angle (range: 0.002748-179.978841)", min_value=0.002748, max_value=179.978841)
    Elbow_Angle = st.number_input("Elbow_Angle (range: 0.000974-179.998046)", min_value=0.000974, max_value=179.998046)
    Hip_Angle = st.number_input("Hip_Angle(range: 107.196850-179.996908)", min_value=107.196850, max_value=179.996908)

with col2:
    Knee_Angle	 = st.number_input("Knee_Angle (range: 114.324207-179.998867)", min_value=114.324207, max_value=179.998867)
    Ankle_Angle = st.number_input("Ankle_Angle (range: 148.849401-179.998854)", min_value=148.849401, max_value=179.998854)
    Elbow_Ground_Angle = st.number_input("Elbow_Ground_Angle(range: 90.0-90.0)", min_value=90.0, max_value=90.0)

with col3:
    Hip_Ground_Angle = st.number_input("Hip_Ground_Angle(range: 90.0-90.0)", min_value=90.0, max_value=90.0)
    Knee_Ground_Angle = st.number_input("Knee_Ground_Angle (range: 90.0-90.0)", min_value=90.0, max_value=90.0)
    Ankle_Ground_Angle = st.number_input("Ankle_Ground_Angle (range: 90.0-90.0)", min_value=90.0, max_value=90.0)

# Prediction
if st.button("Predict"):
    input_data = pd.DataFrame({
        'Shoulder_Angle': [Shoulder_Angle],
        'Elbow_Angle': [Elbow_Angle],
        'Hip_Angle': [Hip_Angle],
        'Knee_Angle': [Knee_Angle],
        'Ankle_Angle': [Ankle_Angle],   
        'Elbow_Ground_Angle': [Elbow_Ground_Angle], 
        'Hip_Ground_Angle': [Hip_Ground_Angle], 
        'Knee_Ground_Angle': [Knee_Ground_Angle], 
        'Ankle_Ground_Angle': [Ankle_Ground_Angle]
    })
    prediction = model.predict(input_data)

    # Display results with colors and emojis
    if prediction[0] == 0:
        st.markdown("<h2 style='color:green;'>Jumping Jacks</h2>", unsafe_allow_html=True)
    elif prediction[0] == 1:
        st.markdown("<h2 style='color:green;'>Push Ups</h2>", unsafe_allow_html=True)
    elif prediction[0] == 2:
        st.markdown("<h2 style='color:green;'>Squats</h2>", unsafe_allow_html=True)
