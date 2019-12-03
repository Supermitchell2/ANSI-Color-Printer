# Handles the addition of ANSI color codes for color printing in certain terminals
class ANSIColorPrinter(object):
	# Adds color to the string message
	# Available colors are black, red, green, yellow, blue, purple, teal, and white
	def add_color(self, message, color, vibrant = False, highlight = False):
		if color == "black":
			color_id = 90
		elif color == "red":
			color_id = 91
		elif color == "green":
			color_id = 92
		elif color == "yellow":
			color_id = 93
		elif color == "blue":
			color_id = 94
		elif color == "purple":
			color_id = 95
		elif color == "teal":
			color_id = 96
		elif color == "white":
			color_id = 97
		else:
			return message
		if vibrant and not highlight:
			color_id = str(color_id - 60)
		if highlight and not vibrant:
			color_id = str(color_id - 50)		
		return "\033[" + str(color_id) + "m" + message + "\033[0m"
	
	# Prints a table containing each of the possible colors
	def print_color_table(self):
		for color_id in range(1, 100):
			print("\033[" + str(color_id) + "m Color " + str(color_id) + " \033[0m")
