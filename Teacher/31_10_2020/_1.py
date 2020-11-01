lst = input('Enter: ').strip().split()
answ = {}

for i in lst:
    i = len(i)
    if i not in answ.keys():
        answ[i] = 1
    elif i in answ.keys():
        answ[i] += 1

print(answ)
