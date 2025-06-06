import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str) -> str:
    city = city.strip().title()  # Normalize formatting
    if not OPENWEATHER_API_KEY:
        return "Missing OpenWeatherMap API key."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}"

    data = response.json()
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]

    return f"The current weather in {city} is {weather} with a temperature of {temp}°C (feels like {feels_like}°C)."
