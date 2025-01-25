import os
import requests
import logging
from dotenv import load_dotenv
from flask import Flask, jsonify

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# SerpAPI configuration
SERP_API_URL = "https://serpapi.com/search.json"
SERP_API_KEY = os.getenv('SPORTS_API_KEY')

# Check if API key is set
if not SERP_API_KEY:
    logger.error("API key not found in .env file.")
    raise ValueError("API key not found in .env file.")

@app.route('/')
def home():
    return "Flask app is running!"

@app.route('/sports', methods=['GET'])
def get_nfl_schedule():
    """
    Fetches the NFL schedule from SerpAPI and returns it as JSON.
    """
    try:
        # Query SerpAPI
        params = {
            "engine": "google",
            "q": "nfl schedule",
            "api_key": SERP_API_KEY
        }
        response = requests.get(SERP_API_URL, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Extract games from sports_results
        games = data.get("sports_results", {}).get("games", [])
        if not games:
            return jsonify({"message": "No NFL schedule available.", "games": []}), 200

        # Format the schedule into JSON
        formatted_games = []
        for game in games:
            teams = game.get("teams", [])
            if len(teams) == 2:
                away_team = teams[0].get("name", "Unknown")
                home_team = teams[1].get("name", "Unknown")
            else:
                away_team, home_team = "Unknown", "Unknown"

            game_info = {
                "away_team": away_team,
                "home_team": home_team,
                "venue": game.get("venue", "Unknown"),
                "date": game.get("date", "Unknown"),
                "time": f"{game.get('time', 'Unknown')} ET" if game.get("time", "Unknown") != "Unknown" else "Unknown"
            }
            formatted_games.append(game_info)

        return jsonify({"message": "NFL schedule fetched successfully.", "games": formatted_games}), 200

    except requests.exceptions.RequestException as e:
        logger.error(f"Request Exception: {e}")
        return jsonify({"message": "An error occurred while fetching the NFL schedule.", "error": str(e)}), 500
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({"message": "An unexpected error occurred.", "error": str(e)}), 500

if __name__ == '__main__':
    logger.info("Starting NFL schedule fetcher web service")
    app.run(host='0.0.0.0', port=8080)
