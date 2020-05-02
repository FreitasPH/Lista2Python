class Eletrodomestic():

	def turn_off():
		print("It returned to the normal temperature")

class Fridge(Eletrodomestic):

	def turn_on():
		print("It's cold!")

class Oven(Eletrodomestic):
	def turn_on():
		print("It's hot!")

Fridge.turn_on()
Fridge.turn_off()
Oven.turn_on()
Oven.turn_off()
