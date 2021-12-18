from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from flask.wrappers import Request
from jinja2 import environment
import requests

from auth import request_weather
from parse_data import weather_parse_data

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')
 

@app.route('/w',methods=['POST', 'GET'])
def searching():
    
    weather_city = request.form["city"]
    weather_data_city = request_weather(weather_city)

    if weather_data_city == 'city-not-found':
        return redirect("/four-o-four.html")

    weather_data_new = weather_parse_data(weather_data_city)
    
    scale = request.form["scale"]

    if request.method == 'POST':
        if scale == 'celsius':

            for values in range(len(weather_data_new['stats'])):
                weather_data_new['stats'][values] = round(weather_data_new['stats'][values] - 273.15,2)

        elif scale == 'fahrenheit':

            for values in range(len(weather_data_new['stats'])):
                weather_data_new['stats'][values] = round((weather_data_new['stats'][values] -273.15)*9/5 + 32,2)

    return render_template('w.html', weather_data=weather_data_new)

@app.errorhandler(404)
def error(e):
    return render_template('four-o-four.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
