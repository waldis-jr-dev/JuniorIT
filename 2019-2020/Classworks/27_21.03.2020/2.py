a  = {}
for i in range(10):
    a[i] = i**2
print(a)
'''keys = []
values = []
for j in a.keys():
    keys.append(j)
    values.append(a[j])
b = {}
for j in range(len(keys)):
    b[values[j]] = keys[j]
print(b)'''
for i in list(a.keys()):
    a[a[i]] = i
    if i != a[i]:
        a.pop(i)
print(a)
