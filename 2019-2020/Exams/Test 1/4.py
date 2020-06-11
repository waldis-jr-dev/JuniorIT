str1 = input('Enter string: ')
new = ''

x = 0
y = 3
while x < len(str1):
    new += str1[x:y:][::-1]

    x += 3
    y += 3
print(new)
