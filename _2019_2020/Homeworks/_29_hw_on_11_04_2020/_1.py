import random


def ispalindrom(numb=0):
    if str(numb) != str(numb)[::-1]:
        raise TypeError("Ne polindrom")


def rand_digit(x=0, y=1):
    while True:
        yield random.randint(x, y)


generator = rand_digit(1, 10000)
ch = 0
answ = 0
while ch < 100:
    num = next(generator)
    try:
        ispalindrom(num)
    except TypeError:
        continue
    answ += num
    ch += 1
print(answ)
