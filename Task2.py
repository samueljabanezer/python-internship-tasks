import requests
import json
 
def fetch_weather(city_name, latitude, longitude):
    """Fetch and display current weather for a given city."""
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current_weather=true"
    )
    try:
        print(f"Fetching weather for {city_name}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # raises error for 4xx/5xx
 
        data = response.json()
        weather = data["current_weather"]
 
        print(f"\n--- Weather Report: {city_name} ---")
        print(f"  Temperature : {weather["temperature"]} °C")
        print(f"  Wind Speed  : {weather["windspeed"]} km/h")
        print(f"  Weather Code: {weather["weathercode"]}")
        print(f"  Time        : {weather["time"]}")
 
    except requests.exceptions.ConnectionError:
        print("Error: No internet connection.")
    except requests.exceptions.Timeout:
        print("Error: Request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except KeyError as e:
        print(f"Unexpected API response format: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
 
# Fetch for multiple cities
fetch_weather("Chennai", 13.08, 80.27)
fetch_weather("Mumbai", 19.07, 72.87)
fetch_weather("Delhi", 28.61, 77.21)
