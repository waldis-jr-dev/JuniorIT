str1 = input('Enter string: ')
t = 0
new = ' '
while t < len(str1) :
    if str1[t].isdigit() and int(str1[t]) % 3 != 0 :
        new += str1[t]
    elif not str1[t].isdigit() :
        new += str1[t]
    t += 1
print(new)