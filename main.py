import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""

weather_params = {
    "lat": 36.162663,
    "lon": -86.781601,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]