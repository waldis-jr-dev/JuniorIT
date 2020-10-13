class Lol:
    kek = 'mem'

    def __init__(self, bob):
        self.bob = bob

    def __repr__(self):
        return f'Lol object. bob = {self.bob}; kek = {self.kek}'


a = Lol('Di')
print(a.__repr__())
