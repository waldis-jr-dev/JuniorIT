string = input('Enter string: ')
new = ' '
b = 0

while b < len(string):
    s = string[b]
    if s.isupper():
        new +=  s+' '
    elif s.isdigit():
        new += s + str(int(s)*2 )
    else:
        new += s
    b += 1
print(new)