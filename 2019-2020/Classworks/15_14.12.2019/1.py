a = [[1, 2], 3, 'a', 7, [2, 9], [3]]
b = []
for i in a:
    if isinstance(i,list):
        for u in i:
            b.append(u)
    else:
        b.append(i)
print(b)