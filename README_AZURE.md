# Weather app with Azure Static Web Apps and Azure Functions

This project is now structured as a simple web app that can be deployed to Azure Static Web Apps.

## Overview

The app has two parts:

1. Frontend
   - A static website built with HTML, CSS, and JavaScript.
   - It calls an Azure Function API to get the weather.

2. Backend
   - An Azure Function named weather.
   - It detects the public IP of the visitor, finds the location from that IP, and fetches the current weather.

## Files in this project

- index.html
  - The page that users see in the browser.
  - It contains the title, button, and result area.

- styles.css
  - The visual design of the page.

- app.js
  - The JavaScript that calls the Azure Function.
  - It sends a request to /api/weather and shows the result on the screen.

- api/weather/__init__.py
  - The Azure Function code.
  - It runs Python logic to:
    - get the public IP,
    - resolve the location from the IP,
    - fetch weather information,
    - return the result as JSON.

- api/weather/function.json
  - The Azure Functions binding file.
  - It tells Azure that this Python function should be exposed as an HTTP endpoint at /api/weather.

## How the app works

1. The browser loads index.html.
2. JavaScript in app.js runs and calls the API endpoint /api/weather.
3. The Azure Function receives the request.
4. The function uses external services:
   - ipify to get the public IP,
   - ipapi to get the geolocation,
   - open-meteo to get the weather forecast.
5. The function returns JSON with:
   - the detected location,
   - temperature,
   - weather condition,
   - humidity,
   - wind speed.
6. The frontend displays the returned information to the user.

## Why this is a good Azure setup

Azure Static Web Apps is ideal for the frontend, because it hosts the static files easily and securely.

Azure Functions is ideal for the backend logic because it lets you run Python code without managing a full server.

This separation keeps the app simple:
- static frontend for the UI,
- serverless function for the logic.

## Local development

You can test the frontend and backend locally.

### 1. Run the frontend
Open index.html in a browser, or use a simple local server.

### 2. Run the Azure Function locally
You need the Azure Functions Core Tools and Python installed.

From the project folder, run:

```bash
func start
```

Then open:

```text
http://localhost:7071/api/weather
```

## Azure deployment

### Deploy the frontend and API together
In Azure Static Web Apps, you can deploy the project directly from GitHub.

Recommended deployment steps:

1. Create a new Static Web App in the Azure portal.
2. Connect your GitHub repository.
3. Set the app location to the project root.
4. Set the API location to api.
5. Deploy.

Azure Static Web Apps will automatically detect the frontend files and the Azure Functions API folder.

## Important note for Python on Azure

This project uses Python for the Azure Function. Azure Functions requires the function app to be structured correctly, and dependencies need to be installed in the environment.

For a production deployment, you usually also add:

- requirements.txt with Azure Functions dependencies,
- a host.json file if you need extra settings.

## Next improvement ideas

You can extend the app to:

- show a more detailed forecast,
- support multiple languages,
- use a weather API key for more advanced features,
- add a map or icons for the current conditions,
- save favorite locations.

## Summary

This app demonstrates a simple and modern architecture:

- Static frontend hosted in Azure Static Web Apps
- Python Azure Function handling the backend logic
- public IP detection plus weather lookup

If you want, I can next help you create the actual Azure deployment files and a full working configuration for Azure Static Web Apps.
