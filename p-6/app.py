from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load("house_price_model.pkl")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "House Price Prediction API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Convert data into NumPy array
        features = np.array(data["features"]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)[0]

        # Return prediction as JSON
        return jsonify({"predicted_price": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
