from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load your trained model (update with actual model file)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "ML Model API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    prediction = model.predict(np.array(data["features"]).reshape(1, -1))
    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
