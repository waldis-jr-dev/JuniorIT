a = []
for i in range(10, 10000):
    if i % 8 == 0 and i % 17 == 0 and i % 3 != 0:
        a.append(i)
print(a)