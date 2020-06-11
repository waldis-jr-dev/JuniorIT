str1 = input('Enter string: ')
new = 0
for i in str1:
    if i.isdigit() and int(i) % 3 == 0:
        new += int(i)
print(new)