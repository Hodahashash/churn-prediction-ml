import pandas as pd

def preprocess_input(data: dict):
    df = pd.DataFrame([data])
    return df
