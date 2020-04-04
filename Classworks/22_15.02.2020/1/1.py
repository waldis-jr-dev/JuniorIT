file = open('victim.py','r')

info = file.readlines()
file.close()

update = ", 'EROR'"
result = []

for i in info:
    if 'print' not in i:
        result.append(i)
    else:
        line = ''
        for j in i:
            if j != ')':
                line += j
            else:
                line += update + ')'
        result.append(line)

file = open('victim1.py', 'w')
for i in result:
    file.write(i)
file.close()
