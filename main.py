from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('kmean.joblib')
scaler = joblib.load('scaler.joblib')

app = FastAPI()

# Define the input features that the user will provide
class InputFeatures(BaseModel):
    Price: float
    Rating: float
    Spa: int
    Wellness_Centre: int
    Swimming_Pool: int
    Fitness_Centre: int
    Room_Service: int
    Facilities: int
    Airport_Shuttle: int

# Function to calculate the Luxury Score and Satisfaction Score
def calculate_scores(features: InputFeatures):
    # Weighted Features
    weighted_price = features.Price * 2
    weighted_rating = features.Rating * 2
    
    # Custom Scoring System: Luxury Score
    luxury_score = (
        weighted_price +
        weighted_rating +
        (features.Spa + features.Wellness_Centre + features.Swimming_Pool + features.Fitness_Centre) * 1.5
    )
    
    # Custom Scoring System: Satisfaction Score
    satisfaction_score = (
        features.Rating * 2 +
        (features.Room_Service + features.Facilities + features.Airport_Shuttle)
    )
    
    return luxury_score, satisfaction_score

# Preprocessing function to scale the features and prepare them for the model
def preprocessing(input_features: InputFeatures):
    luxury_score, satisfaction_score = calculate_scores(input_features)
    
    # Features the model was trained on
    feature_array = np.array([luxury_score, satisfaction_score])
    
    # Scale the features
    scaled_features = scaler.transform([feature_array])
    
    return scaled_features

# Mapping of cluster predictions to user-friendly descriptions
cluster_mapping = {
    0: "Low price and low quality",
    1: "Mid price and high quality",
    2: "Low price and high quality",
    3: "High price and high quality"
}

@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}

@app.get("/try/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/predict")
async def predict(input_features: InputFeatures):
    # Preprocess the input features
    data = preprocessing(input_features)
    
    # Make a prediction using the trained model
    y_pred = model.predict(data)
    
    # Map the prediction to the corresponding label
    prediction_label = cluster_mapping.get(int(y_pred[0]), "Unknown cluster")
    
    return {"cluster": int(y_pred[0]), "The Hotel is ": prediction_label}
