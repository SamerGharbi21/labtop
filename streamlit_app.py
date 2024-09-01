import streamlit as st
import requests

# URL of the FastAPI server
API_URL = "https://labtop.onrender.com/predict"

# Streamlit application layout
st.title("Hotel Clustering Prediction")

st.write("Enter the features of the hotel:")

# Collect user input
price = st.number_input("Price", min_value=0.0, step=0.1)
rating = st.number_input("Rating", min_value=0.0, step=0.1)
spa = st.number_input("Spa (0 or 1)", min_value=0, max_value=1)
wellness_centre = st.number_input("Wellness Centre (0 or 1)", min_value=0, max_value=1)
swimming_pool = st.number_input("Swimming Pool (0 or 1)", min_value=0, max_value=1)
fitness_centre = st.number_input("Fitness Centre (0 or 1)", min_value=0, max_value=1)
room_service = st.number_input("Room Service (0 or 1)", min_value=0, max_value=1)
facilities = st.number_input("Facilities (0 or 1)", min_value=0, max_value=1)
airport_shuttle = st.number_input("Airport Shuttle (0 or 1)", min_value=0, max_value=1)

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
