import requests

api_key = "key"

parameters = {
    "lat": 43.653225,
    "lon": -79.383186,
    "appid": api_key,
    "exclude": "minutely,daily,current"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
data_slice = weather_data["hourly"][:12]

will_rain = False
for weather_hourly in data_slice:
    condition_code = weather_hourly["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")

# print(weather_data["hourly"][0]["weather"][0]["id"])


