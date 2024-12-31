import requests
from twilio.rest import Client


account_sid = "ACf4cdf1702ab028ceb2cacf74bbbdc739"
auth_token = "251be7f74026db6860b12a0c66fef83e"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "d529f466e0ff8177cb0b76fd3df0d276"

weather_params = {
    "lat": 49.492592,
    "lon": 0.106500,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="+18558287490",
        body="It's going to rain today. Please bring an umbrella.",
        to="+16508346809"
    )
    print(message.status)