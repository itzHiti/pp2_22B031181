class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("Point values (x; y):", self.x, ";", self.y)
    def move(self, newx, newy):
        self.x += newx
        self.y += newy
        print("New values (x; y):", self.x, ";", self.y)
    def dist(self, Point):
        self.x = abs(Point.x - self.x) # one of them will be greater than another, hence we
        self.y = abs(Point.y - self.y) # should use abs() function to get positive results
        print("Distance in x:", self.x, "; Distance in y:", self.y)

'''
p1 = Point(6,9)
p2 = Point(4,2)
p1.show()
p1.move(1,1)
p1.dist(p2)
'''