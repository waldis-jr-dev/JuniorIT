import random


def fk(a, b, lng):
    lis = []
    for i in range(lng):
        lis.append(random.randint(a,b))
    return lis


a = int(input('a = '))
b = int(input('b = '))
lng = int(input('len = '))
print(fk(a, b, lng))
