import os
from collections import Counter


class FileMaker:
    def __init__(self, name):
        self.name = name

    def create(self):
        with open(self.name, 'w') as file:
            pass

    def weight(self):
        return str(os.path.getsize(self.name)) + ' bytes'

    def unique_symbols(self):
        with open(self.name, 'r') as file:
            symbols = [symbol for line in file.readlines() for symbol in line]
        counted_symbols = Counter(symbols)
        return len([symbol for symbol in counted_symbols.keys() if counted_symbols[symbol] == 1])

    def end_append(self, symbols):
        with open(self.name, 'a') as file:
            file.write(symbols)

    def start_append(self, symbols):
        with open(self.name, 'r') as file:
            lines = file.readlines()
        with open(self.name, 'w') as file:
            file.write(symbols + ''.join(lines))


test = FileMaker('test.txt')
