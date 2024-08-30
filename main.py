from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

model = joblib.load('kmean.joblib')
scaler = joblib.load('scaler.joblib')

app = FastAPI()

class InputFeatures(BaseModel):
    Swimming_Pool: float
    Room_Service: float
    Fitness_Centre: float 
    Airport_Shuttle: float
    Highspeed_Internet: float
    Airconditioning: float

def preprocessing(input_features: InputFeatures):
    dict_f = {
        'Swimming_Pool': input_features.Swimming_Pool,
        'Room_Service': input_features.Room_Service,
        'Fitness_Centre': input_features.Fitness_Centre,
        'Airport_Shuttle': input_features.Airport_Shuttle,
        'Highspeed_Internet': input_features.Highspeed_Internet,
        'Airconditioning': input_features.Airconditioning,
    }
    feature_list = [dict_f[key] for key in sorted(dict_f)]
    return scaler.transform([feature_list])

@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}

@app.get("/try/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    y_pred = model.predict(data)  # Use predict instead of fit_predict
    return {"cluster": int(y_pred[0])}
