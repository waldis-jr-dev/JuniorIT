str1 = input('Enter string: ')
new = ''
for i in str1:
    if i.isdigit() and i != '0':
        new += i
    if not i.isdigit() and new[len(new) - 1:] != ' ':
        new += ' '
print(new)