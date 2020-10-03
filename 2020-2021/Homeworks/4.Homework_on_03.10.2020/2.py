a = (1, 5, 2, 3, 4, 5, 4, 3, 1, 5)
b = max({i: a.count(i) for i in set(a)}.items(), key= lambda x: x[1])[0]
print(b)
