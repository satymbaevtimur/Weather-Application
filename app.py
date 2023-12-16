from flask import Flask, render_template, request

import requests

app = Flask(__name__)
weather_api_token = '800b1154a23f431d947180647231512'

@app.route("/", methods=['GET'])
def index():
    city = request.args.get('search', '')
    
    if city != '':
        weather_data = get_weather(city)
    else:
        weather_data = get_weather()
    
    return render_template("index.html", weather_data=weather_data)

def get_weather(city_name=''):
    if city_name != '':
        weather_api_url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_token}&q={city_name}"
    else:
        weather_api_url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_token}&q=London"
    response = requests.get(weather_api_url)


    return response.json()

@app.route('/test')
def test():
    weather_api_url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_token}&q=Astana"
    response = requests.get(weather_api_url)

    return response.json()