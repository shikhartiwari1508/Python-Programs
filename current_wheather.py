import requests
data = requests.get("https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current_weather=true").json()
print(f"Delhi: {data['current_weather']['temperature']}°C")