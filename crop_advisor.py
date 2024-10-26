import streamlit as st
import pickle
import numpy as np

# Import the model
try:
    clf = pickle.load(open('pipe.pkl', 'rb'))
    df = pickle.load(open('df.pkl', 'rb'))
except Exception as e:
    st.error("An error occurred while loading the model. Please check model files and try again.")
    st.stop()

# Title
st.markdown("<h1 style='text-align: center;'>CROP ADVISOR</h1>", unsafe_allow_html=True)

st.markdown("")

# Input fields with validations
N = st.text_input("##### Enter ratio of Nitrogen content in soil:  [Range from 1 to 140]", key="nitrogen_input")
if N and (float(N) < 1 or float(N) > 140):
    st.markdown("<h6 style='color: red;'>Nitrogen content must be between 1 and 140.</h6>", unsafe_allow_html=True)

st.markdown("")
P = st.text_input("##### Enter ratio of Phosphorous content in soil:  [Range from 5 to 145]", key="phosphorous_input")
if P and (float(P) < 5 or float(P) > 145):
    st.markdown("<h6 style='color: red;'>Phosphorous content must be between 5 and 145.</h6>", unsafe_allow_html=True)

st.markdown("")
K = st.text_input("##### Enter ratio of Potassium content in soil:  [Range from 5 to 205]", key="potassium_input")
if K and (float(K) < 5 or float(K) > 205):
    st.markdown("<h6 style='color: red;'>Potassium content must be between 5 and 205.</h6>", unsafe_allow_html=True)

st.markdown("")
Temp = st.text_input("##### Enter Temperature (in °C):  [Range from 0 to 50]", key="temperature_input")
if Temp and (float(Temp) < 0 or float(Temp) > 50):
    st.markdown("<h6 style='color: red;'>Temperature must be between 0 and 50 °C.</h6>", unsafe_allow_html=True)

st.markdown("")
Humid = st.text_input("##### Enter value of relative Humidity (in %):  [Range from 0 to 100]", key="humidity_input")
if Humid and (float(Humid) < 0 or float(Humid) > 100):
    st.markdown("<h6 style='color: red;'>Humidity must be between 0 and 100%.</h6>", unsafe_allow_html=True)

st.markdown("")
ph = st.text_input("##### Enter pH value in soil:  [Range from 0 to 14]", key="ph_input")
if ph and (float(ph) < 0 or float(ph) > 14):
    st.markdown("<h6 style='color: red;'>pH value must be between 0 and 14.</h6>", unsafe_allow_html=True)

st.markdown("")
rain = st.text_input("##### Enter value of Rainfall (in mm):  [Range from 15 to 300]", key="rainfall_input")
if rain and (float(rain) < 15 or float(rain) > 300):
    st.markdown("<h6 style='color: red;'>Rainfall must be between 15 and 300 mm.</h6>", unsafe_allow_html=True)

st.markdown("")
# Predict the crop based on valid inputs
if N and P and K and Temp and Humid and ph and rain:
    if all((1 <= float(N) <= 140,
            5 <= float(P) <= 145,
            5 <= float(K) <= 205,
            0 <= float(Temp) <= 50,
            0 <= float(Humid) <= 100,
            0 <= float(ph) <= 14,
            15 <= float(rain) <= 300)):
        
        # Convert input values to float and create an array
        input_data = np.array([[float(N), float(P), float(K), float(Temp), float(Humid), float(ph), float(rain)]])
        
        # Make the prediction with error handling
        try:
            prediction = clf.predict(input_data)
            # Display the result
            st.markdown(f"<h1 style='color:#4CAF50;'>The Suitable Crop to grow in these conditions is {prediction[0].capitalize()}.</h1>", unsafe_allow_html=True)
        except AttributeError as e:
            st.error("The model encountered a compatibility issue. Please ensure the scikit-learn version matches the one used to train the model.")
            st.text(f"Error details: {e}")
        except Exception as e:
            st.error("An error occurred during prediction. Please check input values.")
            st.text(f"Error details: {e}")
    else:
        st.markdown("<h5 style='color: red;'>Please enter valid values in all fields to enable the prediction of Crop.</h5>", unsafe_allow_html=True)
else:
    st.markdown("<h5 style='color: red;'>Please fill all fields to enable the prediction of Crop.</h5>", unsafe_allow_html=True)
