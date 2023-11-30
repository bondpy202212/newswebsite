from flask import current_app
import requests

from webapp.degree import degree_result

# -------------------------------
def weather_by_city(city_name):	

	params1 = {
		'lat': current_app.config['LAT_CITY'],
		'lon': current_app.config['LON_CITY'],
		'units': 'metric',
		'appid': current_app.config['WEATHER_API_KEY']				
	}
	
	weather_url = current_app.config['WEATHER_URL']	
	try:
		result = requests.get(weather_url, params=params1)
		result.raise_for_status()                 # status answer server (error 4xx, 5xx)
		weather = result.json()

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
									'wind_deg'	: degree_result(weather['wind']["deg"])									
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

