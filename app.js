const resultElement = document.getElementById("result");
const refreshButton = document.getElementById("refreshButton");

async function loadWeather() {
  resultElement.textContent = "Loading weather...";

  try {
    const response = await fetch("/api/weather");
    if (!response.ok) {
      throw new Error(`Request failed with status ${response.status}`);
    }

    const data = await response.json();
    resultElement.innerHTML = `
      <strong>${data.location}</strong><br />
      ${data.temperature}°C • ${data.condition}<br />
      Humidity: ${data.humidity}% • Wind: ${data.wind_speed} km/h
    `;
  } catch (error) {
    resultElement.textContent = `Unable to load weather: ${error.message}`;
  }
}

refreshButton.addEventListener("click", loadWeather);
window.addEventListener("load", loadWeather);
