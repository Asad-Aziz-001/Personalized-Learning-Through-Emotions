from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  

# ---- Load Model ----
MODEL_FILE = "depression_model_final.joblib"

if os.path.exists(MODEL_FILE):
    try:
        model = joblib.load(MODEL_FILE)
        print(f"SUCCESS: {MODEL_FILE} loaded.")
    except Exception as e:
        print(f"ERROR: Failed to load model. {e}")
        model = None
else:
    print(f"ERROR: {MODEL_FILE} not found in current directory.")
    model = None


@app.route('/predict', methods=['POST'])
def predict():
    # 1. Check if model is loaded
    if not model:
        return jsonify({"error": "Model not loaded on server"}), 500

    try:
        # 2. Get features from JSON
        req_data = request.get_json()
        features = req_data.get("features")

        if not features:
            return jsonify({"error": "No features provided"}), 400

        print(f"Received {len(features)} features: {features}")

       
        column_names = [
            'Q3A','Q5A','Q10A','Q13A','Q16A','Q17A','Q21A','Q24A',
            'Q26A','Q31A','Q34A','Q37A','Q38A','Q42A',
            'Q2A','Q4A','Q7A','Q9A','Q15A','Q19A','Q20A','Q23A',
            'Q25A','Q28A','Q30A','Q36A','Q40A','Q41A',
            'age','gender'
        ]

        df = pd.DataFrame([features], columns=column_names)

        # 3. Make prediction
        prediction = model.predict(df)[0]
        print(f"Model Prediction: {prediction}")

        # 4. Send result
        return jsonify({"prediction": str(prediction)})

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/')
def home():
    return "<h1>Mental Wellness API is Running</h1>"


if __name__ == '__main__':
    print("Starting Flask Server...")
    app.run(debug=True, port=5000)
