import pandas as pd
import requests
import time

FIREBASE_URL ='https://gps-tracker-72aed-default-rtdb.firebaseio.com/locations.json'  # root path + .json

df = pd.read_csv('balloon_full_2.csv')

for index, row in df.iterrows():
    data = {
        'latitude': row['lat'],
        'longitude': row['lon'],
        'altitude': row['alt'],
        'speed': row.get('speed', 0)  # optional, fill 0 if not in CSV
    }

    response = requests.post(FIREBASE_URL, json=data)  # <-- overwrite root node
    if response.status_code == 200:
        print(f"Sent: {data}")
    else:
        print(f"Failed to send: {data}, Error: {response.text}")

    time.sleep(0.01)
