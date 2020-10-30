import random


def f(minn, maxx):
    a = random.randint(minn, maxx)
    return a


minn = int(input('Enter minn: '))
maxx = int(input('Enter maxx: '))
print(f(minn, maxx))