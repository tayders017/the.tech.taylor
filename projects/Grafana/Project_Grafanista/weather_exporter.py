from prometheus_client import Gauge, start_http_server
import requests
import time

#Add OpenWeatherMap API key
API_KEY = 'OPENWEATHERMAP_API_KEY'

#Add list of cities to monitor, can be added as city name or city ID
cities = ['Austin', 'Los Angeles', 'Portland', 'New York', 'Stockholm']

#Add URL for fetching weather data from OpenWeatherMap API
OWM_API_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Prometheus metrics to expose
temperature_celsius_gauge = Gauge('city_temperature_celsius', 'Temperature in Celsius', ['city'])
temperature_fahrenheit_gauge = Gauge('city_temperature_fahrenheit', 'Temperature in Fahrenheit', ['city'])
humidity_gauge = Gauge('city_humidity', 'Humidity percentage', ['city'])
pressure_gauge = Gauge('city_pressure', 'Atmospheric pressure in hPa', ['city'])
wind_speed_gauge = Gauge('city_wind_speed', 'Wind speed in meters per second', ['city'])

# Function to fetch weather data from OpenWeatherMap
def get_weather_data(city):
	"""Fetch weather data from OpenWeatherMap for a specific city."""
	params = {
		'q': city,
		'appid': API_KEY,
		'units': 'metric'  # Get temperature in Celsius/other values in metric
	}
	response = requests.get(OWM_API_URL, params=params)
	data = response.json()

	if response.status_code == 200:
		temperature_celsius = data['main']['temp']
		temperature_fahrenheit = (temperature_celsius * 9/5) + 32  # Convert Celsius to Fahrenheit
		humidity = data['main']['humidity']
		pressure = data['main']['pressure']
		wind_speed = data['wind']['speed']

		#Update Prometheus metrics
		temperature_celsius_gauge.labels(city=city).set(temperature_celsius)
		temperature_fahrenheit_gauge.labels(city=city).set(temperature_fahrenheit)
		humidity_gauge.labels(city=city).set(humidity)
		pressure_gauge.labels(city=city).set(pressure)
		wind_speed_gauge.labels(city=city).set(wind_speed)
	else:
		print(f"Failed to get data for {city}, Response code: {response.status_code}")

#Main function to periodically update Prometheus metrics
def collect_weather_data():
	#Update metrics every 1 hour (3600 seconds)
	while True:
		for city in cities:
			get_weather_data(city)
		print("Metrics update, sleeping for 1 hour...")
		time.sleep(3600)
		
if __name__ == '__main__':
	#Start the Prometheus server to expose metrics
	start_http_server(8000)
	print("Prometheus metrics server started at port 8000")
    
	# Start collecting weather data
	collect_weather_data()
