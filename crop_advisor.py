import streamlit as st
import pickle
import numpy as np

# Import the model
clf = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Title
st.markdown("<h1 style='font-size: 50px; text-align: center;'>CROP ADVISOR</h1>", unsafe_allow_html=True)
st.markdown("")


st.markdown('<p style="font-size: 21px ; margin-bottom: -50px">Enter ratio of Nitrogen content in soil:  [Range from 1 to 140]</p>', unsafe_allow_html=True)
N = st.text_input("", key="nitrogen_input")
if N and (float(N) < 1 or float(N) > 140):
    st.markdown("<h6 style='color: red;'>Nitrogen content must be between 1 and 140.</h6>", unsafe_allow_html=True)

st.markdown("")
st.markdown('<p style="font-size: 22px ; margin-bottom: -50px">Enter ratio of Phosphorous content in soil:  [Range from 5 to 145]</p>', unsafe_allow_html=True)
P = st.text_input("", key="phosphorous_input")
if P and (float(P) < 5 or float(P) > 145):
    st.markdown("<h6 style='color: red;'>Phosphorous content must be between 5 and 145.</h6>", unsafe_allow_html=True)

st.markdown("")
st.markdown('<p style="font-size: 22px ; margin-bottom: -50px">Enter ratio of Potassium content in soil:  [Range from 5 to 205]</p>', unsafe_allow_html=True)
K = st.text_input("", key="potassium_input")
if K and (float(K) < 5 or float(K) > 205):
    st.markdown("<h6 style='color: red;'>Potassium content must be between 5 and 205.</h6>", unsafe_allow_html=True)

st.markdown("")
st.markdown('<p style="font-size: 22px ; margin-bottom: -50px"> Enter Temperature (in °C):  [Range from 0 to 50]</p>', unsafe_allow_html=True)
Temp = st.text_input("", key="temperature_input")
if Temp and (float(Temp) < 0 or float(Temp) > 50):
    st.markdown("<h6 style='color: red;'>Temperature must be between 0 and 50 °C.</h6>", unsafe_allow_html=True)

st.markdown("")
st.markdown('<p style="font-size: 22px ; margin-bottom: -50px"> Enter value of relative Humidity (in %):  [Range from 0 to 100]', unsafe_allow_html=True)
Humid = st.text_input("", key="humidity_input")
if Humid and (float(Humid) < 0 or float(Humid) > 100):
    st.markdown("<h6 style='color: red;'>Humidity must be between 0 and 100%.</h6>", unsafe_allow_html=True)

st.markdown("")
st.markdown('<p style="font-size: 22px ; margin-bottom: -50px"> Enter pH value in soil:  [Range from 0 to 14]', unsafe_allow_html=True)
ph = st.text_input("", key="ph_input")
if ph and (float(ph) < 0 or float(ph) > 14):
    st.markdown("<h6 style='color: red;'>pH value must be between 0 and 14.</h6>", unsafe_allow_html=True)

st.markdown("")
st.markdown('<p style="font-size: 22px ; margin-bottom: -50px"> Enter value of Rainfall (in mm):  [Range from 15 to 300]', unsafe_allow_html=True)
rain = st.text_input("", key="rainfall_input")
if rain and (float(rain) < 15 or float(rain) > 300):
    st.markdown("<h6 style='color: red;'>Rainfall must be between 15 and 300 mm.</h6>", unsafe_allow_html=True)

st.markdown("")
if st.button("Predict Crop"):
    if N and P and K and Temp and Humid and ph and rain:
        try:
            input_data = np.array([[float(N), float(P), float(K), float(Temp), float(Humid), float(ph), float(rain)]])

            # Validate input values
            if not (1 <= float(N) <= 140 and 5 <= float(P) <= 145 and 5 <= float(K) <= 205 and 0 <= float(Temp) <= 50 and 0 <= float(Humid) <= 100 and 0 <= float(ph) <= 14 and 15 <= float(rain) <= 300):
                st.error("Please enter valid values within the specified ranges.")
            else:
                prediction = clf.predict(input_data)
                st.success(f"The most suitable crop for these conditions is: {prediction[0].capitalize()}")

        except ValueError:
            st.error("Please enter valid numerical values.")
    else:
        st.error("Please fill all fields to enable the prediction of Crop.")
