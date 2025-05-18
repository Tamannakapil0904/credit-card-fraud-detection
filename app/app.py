from flask import Flask, request, jsonify
import joblib
import numpy as np
import warnings

app = Flask(__name__)

model = joblib.load("models/fraud_model.pkl")
scaler = joblib.load("models/scaler.pkl")


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Credit Card Fraud Detection API is running!"}), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    features = np.array(data["features"]).reshape(1, -1)
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)

    print("✅ Prediction complete! Result:", bool(prediction[0]))
    return jsonify({"fraud": bool(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
