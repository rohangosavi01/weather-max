from flask import Flask, render_template, request
from flask.wrappers import Request
from jinja2 import environment

from auth import request_weather

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/weather',methods=['POST', 'GET'])
def searching():
    weather_city = request.form["city"]
    print(weather_city)
    weather_data_1 = request_weather(weather_city)

    '''IF city not available then redirect statment 
        if data == "Not available":
        redirect for URL ("HTML Template")'''

    return render_template('weather.html', weather_data = weather_data_1)



@app.errorhandler(404)
def error():
    return render_template('index.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
