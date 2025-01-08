import os
import boto3
import json
import subprocess
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize S3 client
s3_client = boto3.client('s3')

BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
FOLDER_NAME = os.getenv('AWS_BUCKET_FOLDER_NAME')
CITIES_FILE = os.path.join(os.getcwd(), 'data/cities.json')

@app.route('/')
def index():
    # List the files in the weather-data folder
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=FOLDER_NAME)
        files = response.get('Contents', [])

        weather_data = []
        for file in files:
            file_key = file['Key']
            response = s3_client.get_object(Bucket=BUCKET_NAME, Key=file_key)
            data = json.loads(response['Body'].read().decode('utf-8'))
            weather_data.append(data)
    except Exception as e:
        weather_data = {'error': str(e)}

    return render_template('index.html', weather_data=weather_data)

@app.route('/add_city', methods=['POST'])
def add_city():
    print("Form submitted")
    data = request.get_json()
    city = data.get('city')
    print(f"Received city: {city}")  # Debugging line
    
    # Update cities.json
    if city:
        try:
            # Ensure 'data' folder exists
            if not os.path.exists('data'):
                os.makedirs('data')
            
            # Define the path to cities.json
            CITIES_FILE = 'data/cities.json'

            if os.path.exists(CITIES_FILE):
                # Open the file and load the data
                with open(CITIES_FILE, 'r') as file:
                    try:
                        cities_data = json.load(file)
                    except json.JSONDecodeError:
                        cities_data = {"cities": []}  # If it's empty or corrupted, initialize this
            else:
                cities_data = {"cities": []}  # Initialize if file doesn't exist

            # Append new city if it's not already in the list
            if city not in cities_data["cities"]:
                cities_data["cities"].append(city)

            # Save the updated data back into the file
            with open(CITIES_FILE, 'w') as file:
                json.dump(cities_data, file, indent=4)

            # Run the weather_dashboard.py script
            subprocess.run(['python3', 'src/weather_dashboard.py'])

        except Exception as e:
            print(f"Error updating cities.json: {e}")
    
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
