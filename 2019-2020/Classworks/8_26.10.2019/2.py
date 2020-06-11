

str1 = input('Enter string:  ')
new = ''
t = 0
numbr = 2
while t < len(str1):

    if not str1[t] == ' ':
        new += str1[t]

    else:
        new = new +' ' + str(numbr)+ '.'
        numbr += 1
    t += 1

print('1.' + new)



