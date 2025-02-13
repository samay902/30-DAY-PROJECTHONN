import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("house_price_model.pkl")

# Streamlit UI
st.title("House Price Prediction")

# Input fields
longitude = st.number_input("Longitude")
latitude = st.number_input("Latitude")
rooms = st.number_input("Total Rooms", min_value=0)
bedrooms = st.number_input("Total Bedrooms", min_value=0)
population = st.number_input("Population", min_value=0)


# Predict button
if st.button("Predict Price"):
    features = np.array([longitude, latitude, rooms, bedrooms, population]).reshape(1, -1)
    prediction = model.predict(features)[0]
    st.write(f"Predicted Price: ${prediction:,.2f}")

