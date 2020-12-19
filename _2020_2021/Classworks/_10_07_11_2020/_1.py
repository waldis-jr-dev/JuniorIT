from abc import ABC, abstractmethod


class AbstractExample(ABC):
    @abstractmethod
    def lol(self):
        pass


class ExampleOne(AbstractExample):
    def lol(self):
        print('kek')


a = ExampleOne()
