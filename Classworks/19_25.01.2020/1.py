import random
a = []
for i in range(50):
    a.append(random.randint(-50, 50))


def f(a):
    summ = 0
    for i in a:
        summ += i
    df = summ / len(a)
    return df




def fu(a):
    c = f(a)
    t = 0
    for i in a:
        if i >= c:
            t += 1
    return t


print(fu(a))
