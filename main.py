import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = ""

weather_params = {
    "lat": 36.162663,
    "lon": -86.781601,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}