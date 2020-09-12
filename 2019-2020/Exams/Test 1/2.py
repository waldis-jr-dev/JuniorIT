str1 = input('Enter string:')
new = ''
t = 0
for i in str1:
    if i == '!' or i == '?':
        t += 1
print(t)