import os


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
            file.seek(0)
            return len(set(file.read()))

    def end_append(self, symbols):
        with open(self.name, 'a') as file:
            file.write(symbols)

    def start_append(self, symbols):
        with open(self.name, 'r') as file:
             lines = file.readlines()
        with open(self.name, 'w') as file:
            file.write(symbols + ''.join(lines))


test = FileMaker('test.txt')
print(test.unique_symbols())
