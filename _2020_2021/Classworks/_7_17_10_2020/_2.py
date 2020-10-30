class FirstName:
    def __init__(self, name):
        self.name = name
        print(FirstName.__dict__)


class LastName(FirstName):
    def __init__(self, name, surname):
        super().__init__(name)
        self.surname = surname
        print(LastName.__dict__)


first = FirstName('Jon')
second = LastName('Jon', 'Conor')
