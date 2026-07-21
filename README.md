# Weather app in Python

This project is now a Python-only web app.

## What it does

The app uses your public IP address to estimate your location and then fetches the current weather for that location.

## How it works

- The Flask app serves a simple web page.
- When you submit the form, the server calls external services to detect your IP and fetch weather data.
- The result is shown directly in the browser.

## Files

- weather_app.py: the Flask server and weather logic
- templates/index.html: the page shown to the user

## Run locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   python weather_app.py
   ```
3. Open the browser at:
   ```text
   http://localhost:8000
   ```

## Notes

The app uses public APIs for:
- IP lookup
- geolocation
- OpenWeatherMap weather data

To use it, set an environment variable named OPENWEATHER_API_KEY with your OpenWeatherMap API key.
