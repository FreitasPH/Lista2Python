class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def slope_from_origin(self):
        return self.y/self.x

slope = Point(4,10).slope_from_origin()
print(slope)

#Se a linha for vertical, o programa vai dar problema, 
#afinal a tangente de 90 graus é infinito
