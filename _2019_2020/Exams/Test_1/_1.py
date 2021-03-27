str1 = input('Enter string: ')
new = ''
for i in str1:
    if i.isdigit():
        if 3 < int(i) < 8:
            new += i
print(new)