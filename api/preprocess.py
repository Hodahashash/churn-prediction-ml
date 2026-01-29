# import pandas as pd

# def preprocess_input(data: dict):
#     df = pd.DataFrame([data])
#     return df
import pandas as pd
import joblib
import sys
from pathlib import Path

# Add the api directory to the path
sys.path.insert(0, str(Path(__file__).parent))

# Load model
model_path = Path(__file__).parent.parent / "models" / "feature_columns.pkl"
feature_columns = joblib.load(model_path)

# feature_columns = joblib.load("../models/feature_columns.pkl")

def preprocess_input(data: dict):
    df = pd.DataFrame([data])
    
    # One-hot encode
    df = pd.get_dummies(df)
    
    # Add missing columns
    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0

    # Keep column order
    df = df[feature_columns]

    return df
