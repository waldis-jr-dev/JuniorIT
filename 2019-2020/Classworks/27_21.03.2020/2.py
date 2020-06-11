a  = {}
for i in range(10):
    a[i] = i**2
print(a)
'''keys = []
values = []
for i in a.keys():
    keys.append(i)
    values.append(a[i])
b = {}
for i in range(len(keys)):
    b[values[i]] = keys[i]
print(b)'''
for i in list(a.keys()):
    a[a[i]] = i
    if i != a[i]:
        a.pop(i)
print(a)
