a = [1, 5, 2, 3, 4, 4, 3, 1, 5]
print({i: a.count(i) for i in set(a)})
