str1 = input('Enter string: ')
t = 0
for i in range(len(str1)):
    if str1[i] == 'k' and str1[i + 1] == 'y':
        t += 1
print(t)