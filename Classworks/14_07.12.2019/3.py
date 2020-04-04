a = []
for i in range(10,100000):
    if i % 21 == 0 and i % 37 == 0 and '0' not in str(i) and '7' not in str(i):
        a.append(i)
print(a)