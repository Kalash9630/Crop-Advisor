import streamlit as st
import pickle
import numpy as np

# Define theme colors and font

primaryColor="#FF4B4B"
backgroundColor="#0E1117"
secondaryBackgroundColor="#262730"
textColor="#FAFAFA"
font="sans serif"


# Add custom CSS
custom_styles = f"""
    <style>
       
        .stApp {{
            background-color: {backgroundColor};
        }}
        input[type="text"] {{
            background-color: {secondaryBackgroundColor};  /* Change this to the desired background color */
            color: {textColor};
            border: 1px solid #D3D3D3;  /* Adding a border for visual clarity */
            padding: 5px;  /* Adjusting padding for better spacing */
            font-family:{font};
        }}
    </style>
"""

# Apply custom styles
st.markdown(custom_styles, unsafe_allow_html=True)

# import the model
clf = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

# Initialize a flag to check if any condition is violated
conditions_violated = False

# title
st.markdown("# <div style='text-align: center;color:aqua'>CROP ADVISOR</div>", unsafe_allow_html=True)

st.markdown("")
st.markdown("")
st.markdown("##### <div style='color:#FAFAFA;'><div style='margin-bottom: -5%;'>Enter ratio of Nitrogen content in soil: [Range from 1 to 140]</div></div>", unsafe_allow_html=True)

N = st.text_input("")
# Check if N is not an empty string and is a valid float
# Check if N is not an empty string and is a valid integer
try:
    if N and not (0 < int(N) <= 140):
        st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of Nitrogen content.</p>", unsafe_allow_html=True)
        conditions_violated = True
except ValueError:
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>Please enter a valid integer for Nitrogen content.</p>", unsafe_allow_html=True)
    conditions_violated = True

st.markdown("")
P = st.text_input("##### Enter ratio of Phosphorous content in soil : [ Range from 5 to 145 ]")
# Check if P is not an empty string and is a valid float
# Similar try-except blocks for P and K
try:
    if P and not (5 <= int(P) <= 145):
        st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of Phosphorous content.</p>", unsafe_allow_html=True)
        conditions_violated = True
except ValueError:
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>Please enter a valid integer for Phosphorous content.</p>", unsafe_allow_html=True)
    conditions_violated = True

st.markdown("")
K = st.text_input("##### Enter ratio of Potassium content in soil :  [ Range from 5 to 205 ] ")

# Check if K is not an empty string and is a valid float
try:
    if K and not (5 <= int(K) <= 205):
        st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of Potassium content.</p>", unsafe_allow_html=True)
        conditions_violated = True
except ValueError:
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>Please enter a valid integer for Potassium content.</p>", unsafe_allow_html=True)
    conditions_violated = True

st.markdown("")
Temp = st.text_input("##### Enter Temperature (in °C) :  [ Range from 0 to 50 ]")
# Check if Temp is not an empty string and is a valid float
# Check if Temp is not an empty string and is a valid float
try:
    if Temp and not (0 <= float(Temp) <= 50):
        st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of Temperature condition.</p>", unsafe_allow_html=True)
        conditions_violated = True
except ValueError:
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>Please enter a valid interger of floating number for Temperature.</p>", unsafe_allow_html=True)
    conditions_violated = True

st.markdown("")
Humid = st.text_input("##### Enter value of relative Humidity (in %) :  [ Range from 0 to 100 ]")
# Check if Humid is not an empty string and is a valid float
# Check if Humid is not an empty string and is a valid float
try:
    if Humid and not (0 <= float(Humid) <= 100):
        st.markdown("<p style='text-align: center;color:red;font-size: 20px'>Enter the percentage of Humidity between 1 to 100.</p>", unsafe_allow_html=True)
        conditions_violated = True
except ValueError:
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>Please enter a valid valid interger of floating number for Humidity.</p>", unsafe_allow_html=True)
    conditions_violated = True

st.markdown("")
ph = st.text_input("##### Enter pH value in soil :  [ Range from 0 to 14 ] ")
# Check if ph is not an empty string and is a valid float
try:
    if ph and not (0 <= float(ph) <= 14):
        st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of pH condition.</p>", unsafe_allow_html=True)
        conditions_violated = True
except ValueError:
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>Please enter a valid interger of floating number for pH.</p>", unsafe_allow_html=True)
    conditions_violated = True


st.markdown("")
rain = st.text_input("##### Enter value of Rainfall (in mm) :  [ Range from 15 to 300 ]")
# Check if rain is not an empty string and is a valid float
try:
    if rain and not (15 <= float(rain) <= 300):
        st.markdown("<p style='text-align: center;color:red;font-size: 20px'>No Crop is suitable to grow in this type of Rainfall condition.</p>", unsafe_allow_html=True)
        conditions_violated = True
except ValueError:
    st.markdown("<p style='text-align: center;color:red;font-size: 20px'>Please enter a valid integer or float value for Rainfall.</p>", unsafe_allow_html=True)
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
