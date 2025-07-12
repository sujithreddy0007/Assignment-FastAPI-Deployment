from fastapi import FastAPI
from app.schema import IrisInput
import joblib
import numpy as np
import os

# Load model and scaler
model = joblib.load(os.path.join("app", "model.pkl"))
scaler = joblib.load(os.path.join("app", "scaler.pkl"))

# Iris class labels
class_names = ["setosa", "versicolor", "virginica"]

# Create FastAPI app
app = FastAPI(title="Iris Prediction API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classifier API"}

@app.post("/predict")
def predict_species(data: IrisInput):
    input_array = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    scaled = scaler.transform(input_array)
    prediction = model.predict(scaled)[0]
    return {
        "prediction": class_names[prediction],
        "input_values": input_array[0],
        "class_index": int(prediction)
    }
