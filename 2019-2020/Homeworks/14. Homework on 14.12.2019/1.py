import random
num = int(input('Enter number: '))
a = []
for i in range(num):
    b = random.randint(1, 100)
    a.append(b)
print(a)
for i in range(len(a) - 1):
    for u in range(len(a) - 1):
        if a[u] <= a[u + 1]:
            a[u],a[u+1] = a[u+1],a[u]
print(a)