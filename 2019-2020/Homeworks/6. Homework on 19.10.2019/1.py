a = input('Enter : ')
b = 0
len = len(a)
answ = ' '

while b < len:
    num = a[b]
    if not num.issupper() and num != ' ':
        answ += num

    b += 1
print(answ)
 
