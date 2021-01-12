class rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def recArea(self):
        return self.width * self.height


rectangle_1 = rectangle(4, 13, 5, 10)

print(rectangle_1.recArea())

def getRectangle (x, y, width, height):
    return "Rectangle( {}, {}, {})".format(x, y, width, height)

print(getRectangle(4, 13, 5, 10))