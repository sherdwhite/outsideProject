from datetime import datetime

import requests

# You can get your own API key from https://api.nasa.gov/
# I would normally store this in an environment variable or pull it from a secret manager
API_KEY = "DEMO_KEY"

def fetch_nasa_apod(date=None):
    if date is None:
        date = datetime.today().strftime("%Y-%m-%d")

    api_url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={date}"
    response = requests.get(api_url)

    if response.status_code != 200:
        return None

    return response.json()
