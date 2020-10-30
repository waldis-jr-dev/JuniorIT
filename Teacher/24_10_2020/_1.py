line = '-1 345 -34'
summa = 0
word = ''
if line[-1] != ' ':
    line += ' '
for i in line:
    if i != ' ':
        word += i
    if i == ' ':
        summa += int(word)
        word = ''
print(summa)
