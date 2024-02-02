from flask import current_app
import requests

from webapp.degree import degree_result

# -------------------------------
def weather_by_city(city_name):	

	params1 = {
		'lat': current_app.config['LAT_CITY'],
		'lon': current_app.config['LON_CITY'],
		'units': 'metric',
		# 'units': 'imperial',
		'appid': current_app.config['WEATHER_API_KEY']				
	}
	
	weather_url = current_app.config['WEATHER_URL']	
	try:
		result = requests.get(weather_url, params=params1)
		result.raise_for_status()                 # status answer server (error 4xx, 5xx)
		weather = result.json()

		print(weather)
		print('temp_C    :' ,round(weather["main"]["temp"], 1))
		print('pressure  :' ,round(weather["main"]["pressure"], 1))
		print('humidity  -:' ,round(weather["main"]["humidity"], 1))
		print('visibility:' ,round((weather["visibility"])/1000, 1))
		print('wind_speed:' ,round((weather['wind']["speed"]), 1))

		if "main" in weather:
			if "temp" in weather["main"]:
				try:
					current_condition = {
									'temp_C'	: round(weather["main"]["temp"], 1),
									'FeelsLikeC': round(weather["main"]["feels_like"], 1),
									'temp_min'	: round(weather["main"]["temp_min"], 1),
									'temp_max'	: round(weather["main"]["temp_max"], 1),
									'pressure'	: round(weather["main"]["pressure"], 1),
									'humidity'	: round(weather["main"]["humidity"], 1),
									'visibility': round((weather["visibility"])/1000, 1),
									'wind_speed': round((weather['wind']["speed"]), 1),
									'wind_deg'	: degree_result(weather['wind']["deg"]),

									'temp_F'	: round((weather["main"]["temp"]*1.8)+32, 1),
									'FeelsLikeF': round((weather["main"]["feels_like"]*1.8)+32, 1),
									'temp_minF'	: round((weather["main"]["temp_min"]*1.8)+32, 1),
									'temp_maxF'	: round((weather["main"]["temp_max"]*1.8)+32, 1),
									'pressure_inHg'	: round(weather["main"]["pressure"]*0.029529983071445, 1),
									'visibility_mi': round((weather["visibility"])/1000*0.621371, 1),
									'wind_speed_mph': round((weather['wind']["speed"])*2.23693629, 1),
									}
					return current_condition
				except(IndexError, TypeError): # (server -> give wrong data)
					return False
			else:
				return False
		else:
			return False

	except(requests.RequestException, ValueError): # Network Error (requests-> not Internet, ValueError-> html address wrong)
		print("--/Newwork Error/--")
		return False
	return False

