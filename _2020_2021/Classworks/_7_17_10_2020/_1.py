class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2


class Square(Rectangle):
    def __init__(self, length, width = None):
        super().__init__(length, width)
        self.width = length


test = Square(12)
print(test.area())
