from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature', methods=['POST'])
def temperature():
    city = request.form['city']

   # Retrieve the API key from the environment variable
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')

    # API endpoint for current weather by city name
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        temperature = data['main']['temp']
        return f'The temperature in {city} is {temperature}°C'
    else:
        return 'City not found'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
