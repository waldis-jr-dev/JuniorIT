import random
with open('abc', 'r') as my_file:
    symbol = ''
    for i in my_file:
        for u in range(0, len(i), 2):
            symbol += i[u]
with open('3_GB', 'wb') as file:
    weight = 0
    maxx = 10*1024*1024
    while weight < maxx:
        info = random.choice(symbol)
        info = info.encode('UTF-8')
        weight += len(info)
        file.write(info)
        if weight >= maxx:
            break
