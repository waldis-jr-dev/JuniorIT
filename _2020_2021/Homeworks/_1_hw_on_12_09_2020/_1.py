resp = input('Entet list : ').split()
answ = {}

for el in resp:
    if el not in answ.keys():
        answ[el] = resp.count(el)

print(answ)
