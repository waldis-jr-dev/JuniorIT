
str1 = input('Enter string: ')
new = ''
t = 0
while t < len(str1):
    if str1[t].isupper():
       new += str1[t]

    if not str1[t].isupper() and new[len(new) - 1: len(new)] != ' ':
       new += ' '

    t += 1
print(new)

'''a = input('Enter: ')
new = ''
for i in a:
    if i != '2':
        new += i
print(new)'''
'''str1 = input('Enter string: ')
answ = 0
for num in str1:
    if num.isdigit():
        answ += int(num)
print(answ)'''
