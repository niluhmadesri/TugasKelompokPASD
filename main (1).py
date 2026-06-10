
from fastapi import FastAPI
from pydantic import BaseModel
import sys
sys.path.insert(0, '/content')
from predictor import predict

app = FastAPI()

class HouseInput(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def home():
    return {"message": "House Price Prediction API is running!"}

@app.post("/predict")
def predict_price(data: HouseInput):
    input_dict = data.dict()
    result = predict(input_dict)
    return result
