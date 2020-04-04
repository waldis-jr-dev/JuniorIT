num = int(input('Enter number: '))
a = []
b = []
for i in range(num):
    b.append(i)
    a.append(b)
    b = b.copy()
print(a)