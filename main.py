import requests
from twilio.rest import Client

api_key = "50b6c4fe525eac6dc5debd6190d17117"

account_sid = "ACe0222a0aef34934c8a3e3770a4a5e3f0"
auth_token = "Your token"

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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+17176706908",
        to="Your phone"
    )
    print(message.status)
# print(weather_data["hourly"][0]["weather"][0]["id"])
