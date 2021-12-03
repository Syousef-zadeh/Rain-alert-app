import requests

api_key = "50b6c4fe525eac6dc5debd6190d17117"

parameters = {
    "lat": 43.653225,
    "lon": -79.383186,
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
print(data)