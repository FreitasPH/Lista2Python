class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_line_to(self, destin):
        a = (self.y - destin.y)/(self.x - destin.x)
        b = self.y - a*self.x
        return (a,b)

print(Point(4, 11).get_line_to(Point(6, 15)))
