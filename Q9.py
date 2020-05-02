class Shape:
	pass

class Plotter:
	pass

class Polygon(Shape, Plotter):
	pass

class RegularPolygon(Polygon):
	pass

class RegularHexagon(RegularPolygon):
	pass

class Square(RegularPolygon):
	pass

class Poly(Plotter, Shape):
	pass

class Shape1(Square, RegularHexagon):
	pass

class Shape2(RegularHexagon, Square):
	pass

polygon = Polygon()
poly = Poly()
shape1 = Shape1()
shape2 = Shape2()

print("Polygon")
print(polygon.__class__.__mro__)
print("Poly")
print(poly.__class__.__mro__)
print("Shape1")
print(shape1.__class__.__mro__)
print("Shape2")
print(shape2.__class__.__mro__)

#We can see hom altering the order of declaration affects the MRO

