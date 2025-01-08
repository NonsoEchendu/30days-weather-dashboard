# 30 Days DevOps Challenge - Weather Dashboard

Day 1: Building a weather data collection system using AWS S3 and OpenWeather API

# Weather Data Collection System - DevOps Day 1 Challenge

## Project Overview
This project is a Weather Data Collection System that demonstrates core DevOps principles by combining:
- External API Integration (OpenWeather API)
- Cloud Storage (AWS S3)
- Infrastructure as Code
- Version Control (Git)
- Python Development
- Error Handling
- Environment Management

## Features
- Fetches real-time weather data for multiple cities
- Displays temperature (°F), humidity, and weather conditions
- Automatically stores weather data in AWS S3
- Supports multiple cities tracking
- Timestamps all data for historical tracking

## MODIFICATIONS
- Containerize app using Docker
- Using Flask, display weather data on a webpage
- Users can search for cities and see results

## Technical Architecture
- **Language:** Python 3.x
- **Cloud Provider:** AWS (S3)
- **External API:** OpenWeather API
- **Dependencies:** 
  - boto3 (AWS SDK)
  - python-dotenv
  - requests

## Prerequisites

**Note these guides are based on running this project on an Ubuntu Linux machine**
- AWS Cli
- python3
- pip3
- flask

**1. Installing AWS Cli**

To install AWS, run

```markdown
sudo apt update
sudo apt install awscli
```

To verify installation, run

```markdown
aws --version
```

You should see output like:

```markdown
aws-cli/2.x.x Python/3.x.x Linux/x86_64
```
**2. Installing Python3**

To install AWS, run

```markdown
sudo apt update
sudo apt install python3
```

To verify installation, run

```markdown
python3 --version
```

You should see output like:

```markdown
Python 3.8.10
```

**3. Installing pip3**

To install AWS, run

```markdown
sudo apt update
sudo apt install python3-pip
```

To verify installation, run

```markdown
pip3 --version
```

You should see output like:

```markdown
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
```

## Project Structure
```markdown
weather-dashboard/
  src/
    __init__.py
    weather_dashboard.py
  static/
    style.css
  templates/
    index.html
  app.py
  .env
  .gitignore
  requirements.txt
```

## Setup Instructions
1. Clone the repository:
```markdown
git clone https://github.com/NonsoEchendu/30days-weather-dashboard.git
```

2. Change directory
```markdown
cd 30days-weather-dashboard
```

3. Install dependencies:
```markdown
pip install -r requirements.txt
```

4. Configure environment variables (.env):
```markdown
OPENWEATHER_API_KEY=your_api_key
AWS_BUCKET_NAME=your_bucket_name
```

5.Configure AWS credentials:
```markdown
aws configure
```

6. Run the application:
```markdown
python3 app.py
```

On terminal, you should see something like:
> <img width="936" alt="Screenshot 2025-01-08 at 14 58 13" src="https://github.com/user-attachments/assets/c875861e-b738-4f15-809e-3895c3d1a1d2" />

To view on the web browser, open `http://127.0.0.1:5000/`
> <img width="1512" alt="Screenshot 2025-01-08 at 18 22 40" src="https://github.com/user-attachments/assets/ed971ef7-7cf8-4403-a019-5e04af16aaef" />

<br>

However, this project has been dockerized, to see how to run it with docker, [click here](url)

## What I Learned

- AWS S3 bucket creation and management
- Environment variable management for secure API keys
- Python best practices for API integration
- Git workflow for project development
- Error handling in distributed systems
- Cloud resource management

## Future Enhancements

- Add weather forecasting
- Implement data visualization
- Add more cities
- Create automated testing
- Set up CI/CD pipeline
