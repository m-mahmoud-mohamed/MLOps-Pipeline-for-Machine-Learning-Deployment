from flask import Flask, request, jsonify
import pickle
import pandas as pd
import json
from xgboost import XGBClassifier

# Load the model
with open('xgboost.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize the Flask app
app = Flask(__name__)

# Define the /predict route to handle JSON requests
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True) 
    json_dict = json.loads(data)
    df = pd.DataFrame.from_dict(json_dict, orient='index').transpose()
    # Make prediction using the model
    prediction = model.predict(df)
    
    # Return prediction as JSON response
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)