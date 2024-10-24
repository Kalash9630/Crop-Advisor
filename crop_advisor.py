import streamlit as st
import pickle
import numpy as np

# Import the model
clf = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Title
st.markdown("<h1 style='text-align: center;'>CROP ADVISOR</h1>", unsafe_allow_html=True)

st.markdown("")

# Function to validate input fields
def validate_input(value, min_value, max_value, field_name):
    try:
        float_value = float(value)
        if float_value < min_value or float_value > max_value:
            st.markdown(f"<h6 style='color: red;'>{field_name} must be between {min_value} and {max_value}.</h6>", unsafe_allow_html=True)
            return None
        return float_value
    except ValueError:
        st.markdown(f"<h6 style='color: red;'>Please enter a valid number for {field_name}.</h6>", unsafe_allow_html=True)
        return None

# Input fields with validations
N = st.text_input("##### Enter ratio of Nitrogen content in soil:  [Range from 1 to 140]", key="nitrogen_input")
N = validate_input(N, 1, 140, "Nitrogen content")

st.markdown("")
P = st.text_input("##### Enter ratio of Phosphorous content in soil:  [Range from 5 to 145]", key="phosphorous_input")
P = validate_input(P, 5, 145, "Phosphorous content")

st.markdown("")
K = st.text_input("##### Enter ratio of Potassium content in soil:  [Range from 5 to 205]", key="potassium_input")
K = validate_input(K, 5, 205, "Potassium content")

st.markdown("")
Temp = st.text_input("##### Enter Temperature (in °C):  [Range from 0 to 50]", key="temperature_input")
Temp = validate_input(Temp, 0, 50, "Temperature")

st.markdown("")
Humid = st.text_input("##### Enter value of relative Humidity (in %):  [Range from 0 to 100]", key="humidity_input")
Humid = validate_input(Humid, 0, 100, "Humidity")

st.markdown("")
ph = st.text_input("##### Enter pH value in soil:  [Range from 0 to 14]", key="ph_input")
ph = validate_input(ph, 0, 14, "pH value")

st.markdown("")
rain = st.text_input("##### Enter value of Rainfall (in mm):  [Range from 15 to 300]", key="rainfall_input")
rain = validate_input(rain, 15, 300, "Rainfall")

st.markdown("")

# Predict the crop based on valid inputs
if all([N, P, K, Temp, Humid, ph, rain]):
    # Convert input values to float and create an array
    input_data = np.array([[N, P, K, Temp, Humid, ph, rain]])
    
    try:
        # Make the prediction
        prediction = clf.predict(input_data)
        
        # Display the result
        st.markdown(f"<h1 style='color:#4CAF50;'>The Suitable Crop to grow in these conditions is {prediction[0].capitalize()}.</h1>", unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f"<h6 style='color: red;'>Error during prediction: {str(e)}</h6>", unsafe_allow_html=True)
else:
    st.markdown("<h5 style='color: red;'>Please fill all fields with valid values to enable the prediction of Crop.</h5>", unsafe_allow_html=True)
