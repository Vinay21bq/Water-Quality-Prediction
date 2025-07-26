import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.models import load_model
import json
import tensorflow as tf

# Load the CNN-LSTM model and scaler
# model_cnn_lstm = load_model("./water_quality_cnn-lstm.h5", compile=False)

from tensorflow import keras
import h5py

model_cnn_lstm = keras.models.load_model("./water_quality_cnn-lstm.h5", compile=False)


# model_cnn_lstm = keras.models.load_model("./water_quality_cnn-lstm.h5", compile=False)


with open("scalar.pkl", "rb") as f:
    scaler = pickle.load(f)

# Streamlit App
st.title("Water Quality Prediction (CNN-LSTM)")

st.write(
    """
    This project predicts water quality using a hybrid CNN-LSTM model. By analyzing key water parameters like temperature, pH, and nitrate levels, 
    the system provides insights into whether the water quality is good or poor.
    """
)

# User Input
temperature = st.number_input("Temperature", format="%.2f")
do = st.number_input("D.O", format="%.2f")
ph = st.number_input("pH", format="%.2f")
conductivity = st.number_input("Conductivity", format="%.2f")
bod = st.number_input("B.O.D", format="%.2f")
nitrate = st.number_input("Nitrate", format="%.2f")
fecalcaliform = st.number_input("Fecalcaliform", format="%.2f")
totalcaliform = st.number_input("Totalcaliform", format="%.2f")

# Prediction
if st.button("Predict"):
    user_input = np.array(
        [
            [
                temperature,
                do,
                ph,
                conductivity,
                bod,
                nitrate,
                fecalcaliform,
                totalcaliform,
            ]
        ]
    )
    scaled_input = scaler.transform(user_input)

    prediction = model_cnn_lstm.predict(scaled_input)

    if prediction > 0.5:
        st.subheader(
            "Is the water is sutiable for drinking: Yes Water quality is Good for drinking"
        )
    else:
        st.subheader(
            "Is the water is sutiable for drinking: No Water quality is Poor for drining"
        )
