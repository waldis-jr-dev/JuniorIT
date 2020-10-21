from math import gcd
from typing import Tuple


def reduce_fraction(numerator, denominator):
    divider = gcd(int(numerator), int(denominator))
    return numerator / divider, denominator / divider


class Fractions:
    def __init__(self, fraction: tuple):
        self.numerator = fraction[0]
        self.denominator = fraction[1]

    def __repr__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other: tuple) -> Tuple[int, int]:
        return reduce_fraction(self.numerator * other[1] + other[0] * self.denominator, self.denominator * other[1])

    def __sub__(self, other: tuple) -> Tuple[int, int]:
        return reduce_fraction(self.numerator * other[1] - other[0] * self.denominator, self.denominator * other[1])

    def __mul__(self, other: tuple) -> Tuple[int, int]:
        return reduce_fraction(self.numerator * other[0], self.denominator * other[1])

    def __truediv__(self, other: tuple) -> Tuple[int, int]:
        return reduce_fraction(self.numerator * other[1], self.denominator * other[0])

    def __pow__(self, power: [int], modulo=None) -> [str, int]:
        if power >= 1:
            return reduce_fraction(self.numerator ** power, self.denominator ** power)
        else:
            return 'Power must greater than 1'


if __name__ == '__main__':
    first = Fractions((16, 8))
    second = Fractions((1, 2))
    print(first / second)
