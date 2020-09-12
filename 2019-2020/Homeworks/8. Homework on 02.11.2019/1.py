str1 = input('Enter string: ')
t = 0
new = ''
while t < len(str1) :
    if str1[t] not in '02357':
        new += str1[t]
    t += 1
print(new)