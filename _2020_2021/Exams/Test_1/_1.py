from abc import ABC, abstractmethod
from typing import Tuple, Union


class AbstractNumber(ABC):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __truediv__(self, other):
        pass


class Number(AbstractNumber):
    def __init__(self, whole_part: Union[str, int], fraction_part: Union[int, str]):
        self.whole_part = str(whole_part)
        self.fraction_part = str(fraction_part)

    def __add__(self, other):
        first, second = self.add_0(self.fraction_part, other.fraction_part)
        fraction_part = first + second
        if len(str(fraction_part)) > len(str(self.fraction_part)) or len(str(fraction_part)) > len(str(other.fraction_part)):
            return Number(self.whole_part+other.whole_part+1, int(str(fraction_part)[1::]))
        return Number(self.whole_part+other.whole_part, fraction_part)

    def __sub__(self, other):
        first, second = self.add_0(self.fraction_part, other.fraction_part)
        fraction_part = first - second
        if fraction_part < 0:
            return Number(int(self.whole_part) - other.whole_part - 1, first - fraction_part)
        return Number(int(self.whole_part) - other.whole_part, fraction_part)

    def __mul__(self, other):
        all_together = (self.whole_part + self.fraction_part) * (other.whole_part + other.fraction_part)
        f = len(str(self.fraction_part)) + len(str(other.fraction_part))
        return Number(all_together[:f:], all_together[f::])

    def __truediv__(self, other):
        all_together = (self.whole_part + self.fraction_part) * (other.whole_part + other.fraction_part)
        f = len(str(self.fraction_part)) + len(str(other.fraction_part))
        return Number(all_together[:f:], all_together[f::])

    @staticmethod
    def add_0(first, second) -> Tuple[int, int]:
        if len(first) == len(second):
            return int(first.lstrip('0')), int(second.lstrip('0'))
        if len(first) > len(second):
            second += '0' * (len(first) - len(second))
            return int(first.lstrip('0')), int(second.lstrip('0'))
        if len(first) < len(second):
            first += '0' * (len(second) - len(first))
            return int(first.lstrip('0')), int(second.lstrip('0'))







