from flask import Flask
import requests as rq
import weather


app = Flask(__name__)
with open('api_key.txt') as f:
        api_key = f.read()

@app.route('/')
def hello_world():
    temp = weather.get_paris_temp(api_key)
    return '<h1>Zappa! </h1>'+str(temp)+"°C in Paris"

@app.route('/write/')
def write_weather():
    temp = weather.get_paris_temp(api_key)
    with open("weather.txt", "w") as f:
        f.write(str(temp))
    return "weather.txt created: "+str(temp)+" °C in Paris"

# We only need this for local development.
if __name__ == '__main__':
 app.run()