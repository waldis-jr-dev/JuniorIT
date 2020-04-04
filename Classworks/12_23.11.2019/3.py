str1 = input('Enter: ')
new = ''
new1 = ''
indt = False
for i in str1:
    if i.isdigit() and indt:
        new1 += i
    elif i.isdigit():
        new += i
    elif not i.isdigit():
        indt = True
if  '+' in str1:
    print(int(new) + int(new1))
if  '-' in str1:
    print(int(new) - int(new1))
if  '*' in str1:
    print(int(new) * int(new1))
if  '/' in str1 and new1 != '0':
    print(int(new) / int(new1))
if  '/' in str1 and new1 == '0':
    print('Error, / on 0')
