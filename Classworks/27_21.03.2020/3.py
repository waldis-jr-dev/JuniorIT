c = {1:0, 12:0, 3:6, 16:0}
answ = {}
for i in c.keys():
    if c[i] not in answ.values():
        answ[i] = c[i]
print(answ)