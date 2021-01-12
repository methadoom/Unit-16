class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def recArea(self):
        return self.length * self.width
    
rectangle = Rectangle(4, 7)
print(rectangle.recArea())