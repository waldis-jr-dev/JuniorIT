class A:
    def __init__(self):
        super().__init__()
        print('A')


class B(A):
    def __init__(self):
        super().__init__()
        print('B')


class C(A):
    def __init__(self):
        super().__init__()
        print('C')


class D(B, C):
    def __init__(self):
        super().__init__()
        print('D')


class E(C, B):
    def __init__(self):
        super().__init__()
        print('E')


class F(D, E):
    pass
