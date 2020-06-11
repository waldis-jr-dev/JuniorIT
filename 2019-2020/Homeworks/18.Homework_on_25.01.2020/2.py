import random


def f():
    lis = []
    for i in range(25):
        lis.append(random.randint(-100, 100))
    print(lis)

    new = []
    summ = 0
    for i in lis:
        i = str(i)
        for u in i:
            summ += u
        new.append(summ)
        summ = 0
    print(new)

    for i in range(len(new)):
        if new[i] > new[i+1]:
            new[i], new[i + 1] = new[i+1], new[i]
    print(new)


f()
