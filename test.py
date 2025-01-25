import os
import requests
import logging
from dotenv import load_dotenv  # Import the load_dotenv function

# Load logging module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()  # This loads the variables from .env into the environment

# Load API key from environment variable
api_key = os.getenv('SPORTS_API_KEY')

if not api_key:
    logger.error("API key not found in .env file.")
    raise ValueError("API key not found in .env file.")

url = 'https://serpapi.com/search.json'

params = {
    'q': 'nfl schedule',
    'engine': 'google',
    'api_key': api_key  # Include the API key here
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    logger.error(f"HTTP Error: {e}")
    raise
except requests.exceptions.RequestException as e:
    logger.error(f"Request Exception: {e}")
    raise

# If you want to parse the response data
data = response.json()
print(data)
