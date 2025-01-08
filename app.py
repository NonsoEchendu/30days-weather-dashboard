import os
from flask import Flask, render_template
import boto3
import json
import requests

app = Flask(__name__)

# Initialize S3 client
s3_client = boto3.client('s3')

BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
FOLDER_NAME = os.getenv('AWS_BUCKET_FOLDER_NAME')

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

if __name__ == '__main__':
    app.run(debug=True)

