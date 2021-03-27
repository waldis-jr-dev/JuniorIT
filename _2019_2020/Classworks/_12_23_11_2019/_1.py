a =  int(input('Enter num: '))
a0 = 1
a1 = 1
an = 0
answ ='1 1'
for i in range(2, a+1):
    an  = a1 + a0
    a0 = a1
    a1 = an
    answ += ' ' + str(an)
print(answ)