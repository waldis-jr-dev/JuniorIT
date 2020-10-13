class Lol:
    kek = 'mem'

    def __init__(self, bob):
        self.bob = bob

    def test(self):
        print(1)

    @classmethod
    def first(cls):
        c = cls.kek
        return c + 'qwerty'

    @classmethod
    def second(cls):
        cc = cls.first()
        return cc

    @staticmethod
    def abc():
        print('static')


a = Lol('Di')
print(a.second())
print(Lol.second())
Lol.test()
