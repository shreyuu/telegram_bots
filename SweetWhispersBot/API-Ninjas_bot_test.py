from flask import Flask
import requests

# Define API URL.
TRIVIA_URL = 'https://api.api-ninjas.com/v1/trivia'

# Initialize Flask.
app = Flask(__name__)

# Define routing.
@app.route('/')
def index():
    resp = requests.get(TRIVIA_URL, headers={'X-Api-Key': 'zySNTDohuRqGSxslulcRGg==MCoHoPEVDWUeYTeo'}).json()
    trivia = resp[0]
    return trivia

# Run the Flask app (127.0.0.1:5000 by default).
app.run()