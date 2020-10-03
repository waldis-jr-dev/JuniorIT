class MyClass:
    def __init__(self, test, *args, **kwargs):
        self.test = test
        print(type(args))
        print(type(kwargs))
        print(test)


a = MyClass('lox')
