str1 = input('Enter string: ')
str2 = input('Enter second string: ')
new = ''
t = 0
while t < len(str1):
    if str1[t] not in str2 :
        new += str1[t]
    t += 1
print(new)