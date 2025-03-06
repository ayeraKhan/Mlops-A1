from flask import Flask, request, jsonify
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load trained model and scaler safely
try:
    model_path = "model.pkl"
    scaler_path = "scaler.pkl"

    if not os.path.exists(model_path) or not os.path.exists(scaler_path):
        raise FileNotFoundError("Model or Scaler file is missing!")

    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)

    with open(scaler_path, "rb") as scaler_file:
        scaler = pickle.load(scaler_file)

except Exception as e:
    print(f"Error loading model: {e}")
    model, scaler = None, None


@app.route("/")
def home():
    return "ML Model API is Running!"


@app.route("/predict", methods=["POST"])
def predict():
    if not model or not scaler:
        return jsonify({"error": "Model/scaler not loaded"}), 500

    data = request.get_json()

    if not data or "features" not in data:
        return jsonify({"error": "Invalid req,features key is required"}), 400

    try:
        features = np.array(data["features"]).reshape(1, -1)
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)
        return jsonify({"prediction": int(prediction[0])})

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {e}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
