import streamlit as st
import pickle
import numpy as np

import os

file_path = os.path.join(os.path.dirname(__file__), 'pipe.pkl')
file_path2 = os.path.join(os.path.dirname(__file__), 'df.pkl')

clf = pickle.load(open(file_path, 'rb'))
df = pickle.load(open(file_path2, 'rb'))

# import the model
# # clf = pickle.load(open('pipe.pkl','rb'))
# df = pickle.load(open('df.pkl','rb'))
# # df = pickle.load(open('pipe.pkl','rb'))


# Initialize a flag to check if any condition is violated
conditions_violated = False

# title
st.markdown("# <div style='text-align: center;color:aqua'>CROP ADVISOR</div>", unsafe_allow_html=True)

st.markdown("")
st.markdown("")
N = st.text_input("##### Enter ratio of Nitrogen content in soil : ")
# Check if N is not an empty string and is a valid float
if N and not (0 < int(N) < 140):
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of Nitrogen content.</p>", unsafe_allow_html=True)
    conditions_violated = True

st.markdown("")
P = st.text_input("##### Enter ratio of Phosphorous content in soil : ")
# Check if P is not an empty string and is a valid float
if P and not (5 < int(P) < 145):
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of Phosphorous content.</p>", unsafe_allow_html=True)
    conditions_violated = True

st.markdown("")
K = st.text_input("##### Enter ratio of Potassium content in soil : ")

# Check if K is not an empty string and is a valid float
if K and not (5 < int(K) < 205):
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of Potassium content.</p>", unsafe_allow_html=True)
    conditions_violated = True

st.markdown("")
Temp = st.text_input("##### Enter Temperature (in °C) :")
# Check if Temp is not an empty string and is a valid float
if Temp and not (0 < float(Temp) < 50):
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of Temperature condition.</p>", unsafe_allow_html=True)
    conditions_violated = True

st.markdown("")
Humid = st.text_input("##### Enter value of relative Humidity (in %) :")
# Check if Humid is not an empty string and is a valid float
if Humid and not (0 < float(Humid) < 100):
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>Enter the percentage of Humidity between 1 to 100.</p>", unsafe_allow_html=True)
    conditions_violated = True

st.markdown("")
ph = st.text_input("##### Enter pH value in soil : ")
# Check if ph is not an empty string and is a valid float
if ph and not (0 < float(ph) < 14):
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of pH condition.</p>", unsafe_allow_html=True)
    conditions_violated = True

st.markdown("")
rain = st.text_input("##### Enter value of Rainfall (in mm) :")
# Check if rain is not an empty string and is a valid float
if rain and not (15 < float(rain) < 300):
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of Rainfall condition.</p>", unsafe_allow_html=True)
    conditions_violated = True

# If any condition is violated, don't proceed with the prediction
if conditions_violated:
    st.markdown("<h3 style='color:red'>Please correct the condition before predicting the crop.</h3>", unsafe_allow_html=True)
else:
    st.markdown("")
    if st.button('Predict Crop'):
        query = np.array([float(N), float(P), float(K), float(Temp), float(Humid), float(ph), float(rain)])
        query = query.reshape(1, 7)
        st.markdown("<h1 style='color:#a5f10b;'>The Suitable Crop to grow in these conditions is " + clf.predict(query)[0].capitalize() + ".</h1>", unsafe_allow_html=True)

