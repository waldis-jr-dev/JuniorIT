import random

def pi(calc):
    num = 0
    for i in range(calc):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if x ** 2 + y ** 2 <= 1:
            num += 1
    return 4*num/calc

num = int(input(''))
print(pi(num))