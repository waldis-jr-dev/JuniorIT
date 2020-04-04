import mod
fu = int(input('first = '))
l = int(input('last = '))


def f(first, last):
    lis = []
    for i in range(first, last):
        if i == 1:
            pass
        elif mod.e(i):
            lis.append(i)
    return lis


print(f(fu, l))
