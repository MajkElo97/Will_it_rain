import requests
# import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
# api_key = os.environ.get("OWM_API_KEY")
Twilio_account_sid = "YOUR TWILIO SSII HERE"
Twilio_auth_token = "YOUR TWILIO TOKEN HERE"  # os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 48.036919,
    "lon": 10.499590,
    "appid": "YOUR OWM_Endpoint ID HERE",
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
rain_possibility = weather_data["list"]
will_rain = False

for hours in rain_possibility[:4]:
    if hours["weather"][0]["main"] == "Rain":  # sprawdzaj 4 pierwsze timestampy
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(Twilio_account_sid, Twilio_auth_token)  # http_client=proxy_client
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+18158531321",
        to="+48516154328"
    )
    print(message.status)  # or print(message.sid)
