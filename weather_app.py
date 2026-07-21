import json
import os
import urllib.request
from pathlib import Path

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


def _load_api_key():
    env_key = os.getenv("OPENWEATHER_API_KEY", "").strip()
    if env_key:
        return env_key

    env_file = Path(__file__).resolve().parent / ".env"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            if key.strip() == "OPENWEATHER_API_KEY":
                return value.strip().strip('"').strip("'")

    return ""


OPENWEATHER_API_KEY = _load_api_key()


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None

    if request.method == "POST":
        try:
            weather_data = get_weather_data()
        except Exception as exc:
            error_message = str(exc)

    return render_template("index.html", weather_data=weather_data, error_message=error_message)


@app.route("/api/weather", methods=["GET"])
def api_weather():
    try:
        return jsonify(get_weather_data())
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


def get_weather_data():
    public_ip = _get_public_ip()
    location = _get_location(public_ip)
    weather = _get_weather(location["latitude"], location["longitude"])

    return {
        "ip": public_ip,
        "location": f"{location['city']}, {location['region']}, {location['country_name']}",
        "temperature": weather["temperature"],
        "condition": weather["condition"],
        "humidity": weather["humidity"],
        "wind_speed": weather["wind_speed"],
    }


def _get_public_ip():
    data = _fetch_json("https://api.ipify.org?format=json")
    return data["ip"]


def _get_location(ip):
    data = _fetch_json(f"https://ipapi.co/{ip}/json/")
    return {
        "city": data.get("city", "Unknown city"),
        "region": data.get("region", "Unknown region"),
        "country_name": data.get("country_name", "Unknown country"),
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
    }


def _get_weather(latitude, longitude):
    if latitude is None or longitude is None:
        raise RuntimeError("Location coordinates were not found")
    if not OPENWEATHER_API_KEY:
        raise RuntimeError("OpenWeatherMap API key is missing. Set the OPENWEATHER_API_KEY environment variable.")

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={latitude}&lon={longitude}&appid={OPENWEATHER_API_KEY}&units=metric&lang=en"
    )
    data = _fetch_json(url)

    return {
        "temperature": round(data["main"]["temp"], 1),
        "humidity": data["main"].get("humidity"),
        "wind_speed": round(data.get("wind", {}).get("speed", 0), 1),
        "condition": data["weather"][0].get("description", "Unknown condition").capitalize(),
    }


def _fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "WeatherPythonApp/1.0"})
    with urllib.request.urlopen(req, timeout=15) as response:
        return json.load(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
