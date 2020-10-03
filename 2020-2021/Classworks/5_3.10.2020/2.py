class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.height = abs(x1 - x2)
        self.length = abs(y1 - y2)

    def perimeter(self):
        return 2 * (self.height + self.length)

    def area(self):
        return self.height * self.length
