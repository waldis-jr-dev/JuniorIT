class Lol:
    kek = 'mem'
    number = 1

    def __init__(self, bob):
        self.bob = bob

    def __repr__(self):
        return f'Lol object. bob = {self.bob}; kek = {self.kek}'

    def __add__(self, other):
        return self.number + other


a = Lol('Di')
print(a.__repr__())
print(a.__add__(5))
