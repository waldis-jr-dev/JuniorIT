str1 = input('Enter string: ')
str2 = input('Enter second string: ')
new = ''
t = 0
while t < len(str1):
    z = 0
    indt = False
    while z < len(str2):
        if str1[t] == str2[z]:
            indt = True
            break
        z += 1
    if not indt :
        new += str1[t]
    t += 1
print(new)




