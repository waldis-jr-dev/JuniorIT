a  = {}
for i in range(100):
    a[i] = i**2
print(a)
b = []
for i in a.keys():
    b.append(i)
    b.append(a[i])
print(b)