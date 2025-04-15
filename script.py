import pandas as pd
import requests
import time

FIREBASE_URL = 'https://gps-tracker-72aed-default-rtdb.firebaseio.com/locations.json'  # Add '.json' to the URL

df = pd.read_csv('balloon_full_2.csv')

for index, row in df.iterrows():
    # Extract the values from the row
    data = {
        'latitude': row['lat'],
        'longitude': row['lon'],
        'altitude': row['alt'],
    }

    # Use POST instead of PUT
    response = requests.post(FIREBASE_URL, json=data)
    if response.status_code == 200:
        print(f"Sent: {data}")
    else:
        print(f"Failed to send: {data}, Error: {response.text}")
    
    time.sleep(5)