# Personal API Service

A simple REST API built with Flask that fetches data from external APIs and returns JSON responses.

## Live API

https://personal-api-hl51.onrender.com

## Features

- Fetch random jokes from an external API
- Retrieve GitHub profile statistics
- REST API endpoints returning JSON responses
- Deployed to the cloud

## Technologies Used

- Python
- Flask
- Requests
- Git & GitHub
- Render (Deployment)

## API Endpoints

### Home

```
GET /
```

### Random Joke

```
GET /joke
```

### GitHub Profile

```
GET /github/<username>
```

Example:

```
GET /github/Alexinthehub
```

## Run Locally

Clone the repository:

```
git clone https://github.com/Alexinthehub/personal_api.git
cd personal_api
```

Create a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

The API will run at:

```
http://127.0.0.1:5000
```

## Deployment

This project is deployed using Render.

## Author

Alex Mwendwa  
GitHub: https://github.com/Alexinthehub
