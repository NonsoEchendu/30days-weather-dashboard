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

```markdown
## Project Structure
weather-dashboard/
  data/
    cities.json
  src/
    __init__.py
    weather_dashboard.py
  static/
    style.css
  templates/
    index.html
  .env
  .gitignore
  requirements.txt

## Setup Instructions
1. Clone the repository:
--bash
git clone https://github.com/NonsoEchendu/30days-weather-dashboard.git

2. Change directory
--bash
cd 30days-weather-dashboard

3. Install dependencies:
--bash
pip install -r requirements.txt

4. Configure environment variables (.env):
OPENWEATHER_API_KEY=your_api_key
AWS_BUCKET_NAME=your_bucket_name

4.Configure AWS credentials:
--bash
aws configure

5. Run the application:
--bash
python3 src/weather_dashboard.py

You should see something like:

> <img width="1291" alt="Screenshot 2025-01-08 at 14 39 28" src="https://github.com/user-attachments/assets/63c2b0f9-f97d-4b4e-a664-a28e8fba2dda" />


```

What I Learned

AWS S3 bucket creation and management
Environment variable management for secure API keys
Python best practices for API integration
Git workflow for project development
Error handling in distributed systems
Cloud resource management

Future Enhancements

Add weather forecasting
Implement data visualization
Add more cities
Create automated testing
Set up CI/CD pipeline
