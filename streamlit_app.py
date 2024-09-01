import streamlit as st
import requests

# URL of the FastAPI server
API_URL = "https://labtop.onrender.com/predict"

# Streamlit application layout
st.set_page_config(page_title="Hotel Clustering Prediction", layout="centered")

# Add a header with an image
st.image("https://via.placeholder.com/800x200.png?text=Hotel+Clustering+Prediction", use_column_width=True)
st.title("Hotel Clustering Prediction")

st.write("Enter the features of your hotel to predict its cluster:")

# Collect user input with styled elements
col1, col2 = st.columns(2)

with col1:
    price = st.slider("Price ($)", min_value=0, max_value=15000, value=500)
    rating = st.slider("Rating (0.0 - 10.0)", min_value=0.0, max_value=10.0, value=1.0)
    spa = st.selectbox("Spa", options=[0, 1])
    wellness_centre = st.selectbox("Wellness Centre", options=[0, 1])

with col2:
    swimming_pool = st.selectbox("Swimming Pool", options=[0, 1])
    fitness_centre = st.selectbox("Fitness Centre", options=[0, 1])
    room_service = st.selectbox("Room Service", options=[0, 1])
    facilities = st.selectbox("Facilities", options=[0, 1])
    airport_shuttle = st.selectbox("Airport Shuttle", options=[0, 1])

# Button to send the data to the FastAPI server
if st.button("Predict", use_container_width=True):
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
        st.success(f"**Cluster:** {result['cluster']}")
        st.info(f"The Hotel is: {result['description']}")
    else:
        st.error("Error in prediction. Please check your inputs and try again.")

# Add footer
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px;
            background-color: #f1f1f1;
            color: #555;
        }
    </style>
    <div class="footer">
        <p>Powered by Streamlit and FastAPI</p>
    </div>
    """, unsafe_allow_html=True)
