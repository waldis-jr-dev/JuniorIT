import random, time
with open('abc', 'r') as my_file:
    symbol = ''
    for i in my_file:
        for u in range(0, len(i), 2):
            symbol += i[u]
start = time.time()
data = []
maxx = 10*1024*1024
for i in range(3):
    weight = 0
    line = []
    while True:
        element = random.choice(symbol)
        line.append(element)
        weight += len(element)
        if weight >= maxx:
            break
    line = ''.join(line)
    data.append(line)

mid = time.time()
ch = 0
file_max = 3*1024*1024*1024
with open('3_GB_fast', 'wb') as file:
    while True:
        a = random.choice(data)
        a = a.encode('UTF-8')
        file.write(a)
        ch += maxx
        if ch >= file_max:
            break
end = time.time()
print('DATA CREATING: ', mid-start)
print('DATA WRITING: ', end - mid)
