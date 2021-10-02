import requests as rq

def get_paris_temp(api_key):
    r = rq.get("https://api.openweathermap.org/data/2.5/weather?q=Paris&units=metric&appid="+api_key)
    temp = r.json()['main']['temp']
    return temp