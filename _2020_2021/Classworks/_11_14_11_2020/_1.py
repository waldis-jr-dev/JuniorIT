class Example:
    b = 'lol'

    def __getattribute__(self, item):
        print('attribute', type(item))
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print('Get attr')
        return 'GT'


ex_instance = Example()
print(ex_instance.c)
