class Point:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def reflect_x(self):
		self.y = -self.y


p = Point(3,5)
p.reflect_x()

print("({0},{1})".format(p.x, p.y))
