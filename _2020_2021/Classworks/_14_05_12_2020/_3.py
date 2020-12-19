class Power:
    def __init__(self, func):
        self._func = func

    def __call__(self, a, b):
        print('I`m as wrapper but __call__ method')
        data = self._func(a, b)
        return data ** 2


@Power
def mul(a, b):
    return a * b


print(mul(4, 6))
