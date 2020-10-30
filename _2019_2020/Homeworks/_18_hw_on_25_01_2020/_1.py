import random


def f():
    a = []
    for i in range(50):
        a.append(random.randint(-50, 50))
    minn = a[0]
    maxx = a[0]
    for i in a:
        if i > maxx:
            maxx = i
        if i < minn:
            minn = i
    print(f"maxx = {maxx}")
    print(f"min = {minn}")


f()
