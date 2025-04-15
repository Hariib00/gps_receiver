import pandas as pd
import requests
import time

FIREBASE_URL = 'https://gps-tracker-72aed-default-rtdb.firebaseio.com/'  # Replace with your URL

df = pd.read_csv('balloon_full_2.csv')

for index, row in df.iterrows():
    # Extract the values from the row
    data = {
        'latitude': row['lat'],
        'longitude': row['lon'],
        'altitude': row['alt'],
        'speed': row['speed'],
    }

    requests.put(FIREBASE_URL, json=data)
    time.sleep(5)
    print(f"Sending: {data}")