import streamlit as st
import requests

API_URL = "https://labtop.onrender.com/predict"

# Set the page title and layout
st.set_page_config(page_title="Hotel Clustering Prediction", layout="centered")

# Title and description
st.title("Hotel Clustering Prediction")
st.write("Enter the features of your hotel:")

# Group input features into a box with three columns
with st.container():
    with st.form(key='hotel_form'):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            price = st.slider("Price ($)", min_value=0, max_value=15000, value=500)
            rating = st.slider("Rating (0.0 - 10.0)", min_value=0.0, max_value=10.0, value=5.0)
        
        with col2:
            spa = st.selectbox("Spa", options=[0, 1])
            wellness_centre = st.selectbox("Wellness Centre", options=[0, 1])
            swimming_pool = st.selectbox("Swimming Pool", options=[0, 1])
        
        with col3:
            fitness_centre = st.selectbox("Fitness Centre", options=[0, 1])
            room_service = st.selectbox("Room Service", options=[0, 1])
            facilities = st.selectbox("Facilities", options=[0, 1])
            airport_shuttle = st.selectbox("Airport Shuttle", options=[0, 1])
        
        # CSS styling to make the button the same width as the columns
        st.markdown(
            """
            <style>
            div.stButton > button {
                width: 100%;
                font-size: 16px;
                padding: 10px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
            }
            div.stButton > button:hover {
                background-color: #45a049;
            }
            </style>
            """, unsafe_allow_html=True
        )

        # Display the submit button spanning all columns
        submit_button = st.form_submit_button(label="Predict")

# Handling form submission
if submit_button:
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

    # Handling the response
    if response.status_code == 200:
        result = response.json()
        
        # Styling the output
        st.markdown(
            f"""
            <div style='padding: 10px; border-radius: 5px; background-color: #f0f0f0; margin-top: 20px;'>
                <h4 style='color: #4CAF50;'>Cluster: {result['cluster']}</h4>
                <p style='font-size: 18px; color: #333;'>{result['description']}</p>
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.error("Error in prediction. Please check your inputs and try again.")
