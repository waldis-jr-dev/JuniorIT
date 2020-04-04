file = open('ostrov.txt', 'r')
answ = 0
for i in file:
    i = i.strip()
    i = i.split()
    i2 = []
    for j in i:
        i2.append(j.lower())
    answ += i2.count('')
file.close()

print(answ)
