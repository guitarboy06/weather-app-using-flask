import requests


def data(city, country, api_key):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}")
    result = res.json()

    temp = result["main"]["temp"]
    temp_k = str(round((temp - 32) / 9))
    humidity = str(result["main"]["humidity"])
    sky = result["weather"][0]["description"]
    wind_speed = str(result["wind"]["speed"])
    icon = result["weather"][0]["icon"]
    return [temp_k, humidity, sky, wind_speed, icon]
