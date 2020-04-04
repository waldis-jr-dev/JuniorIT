idnt = int(input('Enter: '))
x = 1
y = 0
z = 0
new = '1 '
while idnt - 1 > 0:

    z = x + y
    new = new + str(z) + ' '
    y = x
    x = z
    idnt -= 1

print(new)












#OOP !!!