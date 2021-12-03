import requests

api_key = "50b6c4fe525eac6dc5debd6190d17117"

parameters = {
    "lat": 43.653225,
    "lon": -79.383186,
    "appid": api_key,
    "exclude": "minutely,daily,current"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
data = weather_data["hourly"][:12]
print(data)
# print(weather_data["hourly"][0]["weather"][0]["id"])


