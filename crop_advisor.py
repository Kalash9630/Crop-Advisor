import streamlit as st
import pickle
import numpy as np

# Load the model and dataset
clf = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Title
st.markdown("<h1 style='text-align: center;'>CROP ADVISOR</h1>", unsafe_allow_html=True)

# Function to validate input and display an error message
def validate_input(input_value, min_value, max_value, label):
    try:
        val = float(input_value)
        if val < min_value or val > max_value:
            st.markdown(f"<h6 style='color: red;'>{label} must be between {min_value} and {max_value}.</h6>", unsafe_allow_html=True)
            return None
        return val
    except ValueError:
        if input_value:
            st.markdown(f"<h6 style='color: red;'>{label} must be a number.</h6>", unsafe_allow_html=True)
        return None

# Collect and validate user inputs
N = validate_input(st.text_input("##### Enter ratio of Nitrogen content in soil:  [Range from 1 to 140]"), 1, 140, "Nitrogen content")
P = validate_input(st.text_input("##### Enter ratio of Phosphorous content in soil:  [Range from 5 to 145]"), 5, 145, "Phosphorous content")
K = validate_input(st.text_input("##### Enter ratio of Potassium content in soil:  [Range from 5 to 205]"), 5, 205, "Potassium content")
Temp = validate_input(st.text_input("##### Enter Temperature (in °C):  [Range from 0 to 50]"), 0, 50, "Temperature")
Humid = validate_input(st.text_input("##### Enter value of relative Humidity (in %):  [Range from 0 to 100]"), 0, 100, "Humidity")
ph = validate_input(st.text_input("##### Enter pH value in soil:  [Range from 0 to 14]"), 0, 14, "pH value")
rain = validate_input(st.text_input("##### Enter value of Rainfall (in mm):  [Range from 15 to 300]"), 15, 300, "Rainfall")

# Check if all inputs are valid
if None not in (N, P, K, Temp, Humid, ph, rain):
    # Convert input values to a numpy array of dtype float64 for prediction
    input_data = np.array([[N, P, K, Temp, Humid, ph, rain]], dtype=np.float64)

    # Check input shape and type (optional for debugging)
    st.write("Input data shape:", input_data.shape)
    st.write("Input data type:", input_data.dtype)

    # Make the prediction
    try:
        prediction = clf.predict(input_data)
        # Display the result
        st.markdown(f"<h1 style='color:#4CAF50;'>The Suitable Crop to grow in these conditions is {prediction[0].capitalize()}.</h1>", unsafe_allow_html=True)
    except Exception as e:
        st.error("An error occurred during prediction. Please check input values.")
        st.error(f"Error details: {str(e)}")
else:
    st.markdown("<h5 style='color: red;'>Please fill all fields with valid values to enable the prediction of Crop.</h5>", unsafe_allow_html=True)
