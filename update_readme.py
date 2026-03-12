import os
import requests
from datetime import datetime
import pytz

UPPSALA = "Uppsala,SE"
NATAL = "Natal,BR"
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    data = requests.get(url).json()
    temp = round(data["main"]["temp"])
    desc = data["weather"][0]["description"].title()
    return f"{temp}°C, {desc}"

uppsala_weather = get_weather(UPPSALA)
natal_weather = get_weather(NATAL)

tz = pytz.timezone("Europe/Stockholm")
weekday = datetime.now(tz).strftime("%A")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = readme.replace("{{UPPSALA_WEATHER}}", uppsala_weather)
readme = readme.replace("{{NATAL_WEATHER}}", natal_weather)
readme = readme.replace("{{WEEKDAY}}", weekday)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
