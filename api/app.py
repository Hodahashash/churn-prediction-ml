from fastapi import FastAPI
import joblib
import numpy as np
import sys
from pathlib import Path

# Add the api directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from schemas import CustomerData
from preprocess import preprocess_input

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predict customer churn probability",
    version="1.0"
)

# Load model
model_path = Path(__file__).parent.parent / "models" / "final_model.pkl"
model = joblib.load(model_path)

@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}

@app.post("/predict")
def predict_churn(customer: CustomerData):
    data = preprocess_input(customer.dict())
    
    prob = model.predict_proba(data)[0][1]
    prediction = int(prob > 0.5)

    return {
        "churn_probability": round(float(prob), 3),
        "churn_prediction": prediction
    }
