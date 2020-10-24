from typing import Union


class Dot:
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = x
        self.y = y

    @classmethod
    def points_distance(cls, dot1, dot2) -> Union[int, float]:
        return ((dot2.x - dot1.x)**2 + (dot2.y - dot1.y) ** 2) ** 0.5


class Rectangle:
    def __init__(self, dot1: Dot, dot2: Dot) -> None:
        self.dot1 = dot1
        self.dot2 = dot2

    def area(self):
        return abs(self.dot1.x - self.dot2.x) * abs(self.dot1.y - self.dot2.y)

    def perimeter(self):
        per = abs(self.dot1.x - self.dot2.x) + abs(self.dot1.y - self.dot2.y)
        return per * 2 if self.area() != 0 else per


dot_1 = Dot(1, 0)
dot_2 = Dot(3, 0)
print(Dot.points_distance(dot_1, dot_2))

rec = Rectangle(dot_1, dot_2)
print(rec.area())
print(rec.perimeter())
