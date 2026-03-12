import os
import requests
from datetime import datetime
import pytz

# ------------------------------
def replace_between(text, start_marker, end_marker, new_content):
    start = text.find(start_marker)
    end = text.find(end_marker)

    if start == -1 or end == -1:
        raise ValueError(f"Markers {start_marker} or {end_marker} not found in README.")

    start += len(start_marker)
    return text[:start] + new_content + text[end:]
# ------------------------------

# Weather fetching code
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

# Replace sections
readme = replace_between(readme, "<!--UPPSALA_WEATHER-->", "<!--END_UPPSALA_WEATHER-->", uppsala_weather)
readme = replace_between(readme, "<!--NATAL_WEATHER-->", "<!--END_NATAL_WEATHER-->", natal_weather)
readme = replace_between(readme, "<!--WEEKDAY-->", "<!--END_WEEKDAY-->", weekday)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
