import random

lis = []
for i in range(100):
    lis.append(random.randint(0, 20))
summ = 0
for i in lis:
    a = int(i * 0.667)
    summ += a
print(summ)
