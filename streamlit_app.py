import streamlit as st
import requests

API_URL = "https://labtop.onrender.com/predict"

st.title("Hotel Clustering Prediction")

st.write("Enter the features of your hotel:")

price = st.slider("Price", min_value=0, max_value=15000, value=500)
rating = st.slider("rating", min_value=0.0, max_value=10.0, value=1.0)
spa = st.selectbox("Spa", options=[0, 1])
wellness_centre = st.selectbox("Wellness Centre", options=[0, 1])
swimming_pool = st.selectbox("Swimming Pool", options=[0, 1])
fitness_centre = st.selectbox("Fitness Centre", options=[0, 1])
room_service = st.selectbox("Room Service", options=[0, 1])
facilities = st.selectbox("Facilities", options=[0, 1])
airport_shuttle = st.selectbox("Airport Shuttle", options=[0, 1])

if st.button("Predict"):
    # Prepare the input data
    data = {
        "Price": price,
        "Rating": rating,
        "Spa": spa,
        "Wellness_Centre": wellness_centre,
        "Swimming_Pool": swimming_pool,
        "Fitness_Centre": fitness_centre,
        "Room_Service": room_service,
        "Facilities": facilities,
        "Airport_Shuttle": airport_shuttle
    }

    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        result = response.json()
        st.write(f"Cluster: {result['cluster']}")
        st.write(f"The Hotel is : {result['description']}")
    else:
        st.error("Error in prediction")