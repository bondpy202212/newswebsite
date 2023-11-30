
def degree_result(degree):
	if degree >= 337.5 or degree < 22.5:
	    direction = 'N'
	elif degree >= 22.5 and degree < 67.5:
	    direction = 'NE'
	elif degree >= 67.5 and degree < 112.5:
	    direction = 'E'
	elif degree >= 112.5 and degree < 157.5:
	    direction = 'SE'
	elif degree >= 157.5 and degree < 202.5:
	    direction = 'S'
	elif degree >= 202.5 and degree < 247.5:
	    direction = 'SW'
	elif degree >= 247.5 and degree < 292.5:
	    direction = 'W'
	else:
	    direction = 'NW'

	return direction
	