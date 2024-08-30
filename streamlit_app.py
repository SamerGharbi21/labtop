import streamlit as st
import requests

# Set the URL for the FastAPI app
url = "http://127.0.0.1:8000/predict"  # Update with your FastAPI URL

# Create the Streamlit app
st.title("Hotel Amenities Clustering")

# Input fields for the user to provide data, with values 0 (absent) or 1 (present)
swimming_pool = st.slider("Is there a Swimming Pool?", 0, 1, 0)
room_service = st.slider("Is there Room Service?", 0, 1, 0)
fitness_centre = st.slider("Is there a Fitness Centre?", 0, 1, 0)
airport_shuttle = st.slider("Is there an Airport Shuttle?", 0, 1, 0)
highspeed_internet = st.slider("Is there Highspeed Internet?", 0, 1, 0)
airconditioning = st.slider("Is there Airconditioning?", 0, 1, 0)

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
