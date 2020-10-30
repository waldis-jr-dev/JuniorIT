str1 = input('Enter string: ')
new = ''
t = 0
while t + 2 < len(str1):
    if str1[t].islower() and str1[t+1].isupper() and str1[t+2].islower():
        new = new + ' ' + str1[t] + str1[t+1] + str1[t+2]
    t += 1
print(new)
