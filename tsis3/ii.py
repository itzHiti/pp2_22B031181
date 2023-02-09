class Shape(object):
    def area():
        print(0) # <- will always print "0"
    
class Square(Shape):
        def __init__(self, length):
            self.length = length
        def area(self):
            print(self.length * self.length) # because it's square (s = a * a)


class Rectangle(Shape):
    def __init__(self, length, width):
         self.length = length
         self.width = width
    def area(self):
        rectarea = self.length * self.width # because it's rectangle (s = a * b)
        print(rectarea)

'''
Shape.area()
'''
'''
Square(5).area()
'''
'''
Rectangle(3, 4).area()
'''