import streamlit as st
import requests

# Set the URL for the FastAPI app
url = "https://labtop.onrender.com/predict"  # Updated URL

# Create the Streamlit app
st.title("Hotel Amenities Clustering")

# Input fields for the user to provide data using select boxes
swimming_pool = st.selectbox("Is there a Swimming Pool?", [0, 1], index=0)
room_service = st.selectbox("Is there Room Service?", [0, 1], index=0)
fitness_centre = st.selectbox("Is there a Fitness Centre?", [0, 1], index=0)
airport_shuttle = st.selectbox("Is there an Airport Shuttle?", [0, 1], index=0)
highspeed_internet = st.selectbox("Is there Highspeed Internet?", [0, 1], index=0)
airconditioning = st.selectbox("Is there Airconditioning?", [0, 1], index=0)

# Prepare the data to be sent as JSON
data = {
    "Swimming_Pool": swimming_pool,
    "Room_Service": room_service,
    "Fitness_Centre": fitness_centre,
    "Airport_Shuttle": airport_shuttle,
    "Highspeed_Internet": highspeed_internet,
    "Airconditioning": airconditioning
}

# Button to trigger the prediction
if st.button("Predict Cluster"):
    # Send the data to FastAPI and get the response
    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"The predicted cluster is: {result['cluster']}")
    else:
        st.error("Failed to get a prediction. Please try again.")
