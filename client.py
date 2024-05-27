import requests
import pandas as pd
import json
import sys

url = 'http://localhost:5000/predict'
csv_file = sys.argv[1]

df = pd.read_csv(csv_file)
f = open("selected_features_1000.txt", "r")
x= f.readlines()
x= [line.strip() for line in x]
df2=df[x]

# Convert DataFrame to JSON 
data_dict = df2.to_json()
# print(f" Here \n{data_dict}")
response = requests.post(url, json=data_dict)

if response.status_code == 200:
    # Handle the response if it contains valid JSON data
    try:
        response_json = response.json()
        if 'prediction' in response_json:
            predictions = response_json['prediction']
            
            # Convert the predictions to DataFrame and save to CSV
            df2['Prediction'] = predictions

            label_map = {0: "FileInfector", 1: "Adware", 2: "Riskware", 3:"Trojan" , 4: "Zeroday", 5:"Backdoor",  6: "Banker", 7: "Dropper", 8:"NoCategory" , 9: "PUA", 10:"Ransomware",  11: "SMS", 12:"Scareware"  , 13: "Spy", 14:"Benign"}

            df2['Prediction'] = df2['Prediction'].map(label_map)
            
            print(f"Predictions: {df2['Prediction']}")

            df2['Prediction'].to_csv('predictions.csv', index=False)
    except ValueError:
        print("Response does not contain valid JSON data")
else:
    print(f"Request failed with status code: {response.status_code}")
