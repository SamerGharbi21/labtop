import streamlit as st
import requests

# URL of the FastAPI server
API_URL = "http://localhost:8000/predict"

# Streamlit application layout
st.title("Hotel Clustering Prediction")

st.write("Enter the features of the hotel:")

# Collect user input
price = st.number_input("Price", min_value=0.0, step=0.1)
rating = st.number_input("Rating", min_value=0.0, step=0.1)

# Using selectbox for binary features
spa = st.selectbox("Spa", options=[0, 1])
wellness_centre = st.selectbox("Wellness Centre", options=[0, 1])
swimming_pool = st.selectbox("Swimming Pool", options=[0, 1])
fitness_centre = st.selectbox("Fitness Centre", options=[0, 1])
room_service = st.selectbox("Room Service", options=[0, 1])
facilities = st.selectbox("Facilities", options=[0, 1])
airport_shuttle = st.selectbox("Airport Shuttle", options=[0, 1])

# Button to send the data to the FastAPI server
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
    
    # Send the request to the FastAPI server
    response = requests.post(API_URL, json=data)
    
    if response.status_code == 200:
        result = response.json()
        st.write(f"Cluster: {result['cluster']}")
        st.write(f"Description: {result['description']}")
    else:
        st.error("Error in prediction")
