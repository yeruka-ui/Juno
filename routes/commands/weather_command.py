from .command_helper import newJson
import requests
import os

def get_weather(command, confidence, place='Manila'):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric"

    response = requests.get(url).json()

    # Extract attributes
    weather = response['weather'][0]['description'].capitalize()
    temp = response['main']['temp']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']

    content = (
        f"The weather in {place.title()} is {weather}, "
        f"{temp}°C with {humidity}% humidity and winds at {wind_speed} m/s."
    )

    return newJson(command, confidence, content)
