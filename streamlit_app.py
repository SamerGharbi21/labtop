import streamlit as st
import requests

# URL of the FastAPI server
API_URL = "https://labtop.onrender.com/predict"

# Streamlit application layout
st.set_page_config(page_title="Hotel Clustering Prediction", layout="centered")

# Add the header image
header_image_path = "./image.png"
st.image(header_image_path, use_column_width=True)

# Add a title and description
st.title("Hotel Clustering Prediction")
st.write("Enter the features of your hotel to predict its cluster:")

# Organize input fields in a more compact layout
with st.form(key='hotel_form'):
    col1, col2 = st.columns(2)
    
    with col1:
        price = st.slider("Price ($)", min_value=0, max_value=15000, value=500)
        rating = st.slider("Rating (0.0 - 10.0)", min_value=0.0, max_value=10.0, value=5.0)
        spa = st.selectbox("Spa", options=[0, 1])
        wellness_centre = st.selectbox("Wellness Centre", options=[0, 1])

    with col2:
        swimming_pool = st.selectbox("Swimming Pool", options=[0, 1])
        fitness_centre = st.selectbox("Fitness Centre", options=[0, 1])
        room_service = st.selectbox("Room Service", options=[0, 1])
        facilities = st.selectbox("Facilities", options=[0, 1])
        airport_shuttle = st.selectbox("Airport Shuttle", options=[0, 1])

    # Use a container for the button and apply CSS for full-width
    st.markdown(
        """
        <style>
        .full-width-button button {
            width: 100%;
            font-size: 16px;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        .full-width-button button:hover {
            background-color: #45a049;
        }
        </style>
        """, unsafe_allow_html=True
    )

    with st.container():
        submit_button = st.form_submit_button(label="Predict", help="Submit the hotel data for clustering")

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

    if response.status_code == 200:
        result = response.json()
        st.success(f"**Cluster:** {result['cluster']}")
        st.info(f"The Hotel is: {result['description']}")
    else:
        st.error("Error in prediction. Please check your inputs and try again.")
