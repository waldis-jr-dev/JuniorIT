x = input('Number: ')
ch = 0
first = 0
second = 0
while ch < len(x):
    if ch%2 == 0:
        first += int(x[ch])
    else:
        second += int(x[ch])
    ch += 1
if first == second:
    print('Lucky')
else:
    print('Unlucky')
