from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from flask.wrappers import Request
from jinja2 import environment

from authentication import request_weather
from weatherData import customDataDictionary

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST', 'GET'])
def weatherForecasting():
    city = request.form["city"]
    scale = request.form["scale"]

    weatherData = request_weather(city)

    if weatherData == 'city-not-found':
        return redirect("/four-o-four.html")

    weatherData = customDataDictionary(weatherData) 

    if request.method == 'POST':
        if scale == 'celsius':
            degree = 'C'
            for values in range(len(weatherData['stats'])):
                weatherData['stats'][values] = round(weatherData['stats'][values] - 273.15,2)
        
        elif scale == 'fahrenheit':
            degree = 'F'
            for values in range(len(weatherData['stats'])):
                weatherData['stats'][values] = round((weatherData['stats'][values] -273.15)*9/5 + 32,2)

    return render_template('weather.html', weather_data=weatherData, degree=degree)

@app.errorhandler(404)
def error(e):
    return render_template('four-o-four.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
