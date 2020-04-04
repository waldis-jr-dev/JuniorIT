str1 = input('Enter string: ')
new = ''
t = 0
while t < len(str1):
    new += str1[t:t+2][::-1]
    t += 2
print(new)
