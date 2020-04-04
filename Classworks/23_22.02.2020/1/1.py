with open('pi.txt', 'r') as file:
    new = ''
    for i in file:
        new += i.strip()
max_len = 0
pod = ''
ch = 0
while ch < len(new) - 1:
    ch_2 = ch
