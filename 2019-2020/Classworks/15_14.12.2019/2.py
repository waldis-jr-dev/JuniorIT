a = [[1,2,'314'],4,5,'456',[45,56]]
b = []
t = 0
for i in a:
    if isinstance(i,list):
        for j in i:
            if isinstance(j, str):
                for x in i:
                    t += int(x)
            else:
                t += j
            b.append(t)
            t = 0

    if isinstance(i, str):
        for j in i:
            t += int(j)
        b.append(t)
        t = 0
    if isinstance(i, int):
        b.append(i)
print(b)
for i in b:
    t += i
print(t)
input()

