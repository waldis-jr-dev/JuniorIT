def func(string=""):
    string = string.lower()
    simbls = [".", ",", "?", "!", ";", ":"]
    spis = string.split()
    answ = {}
    for i in range(len(spis)):
        if spis[i][-1] in simbls:
            spis[i] = spis[i][:-1:]
        if spis[i] not in answ:
            answ[spis[i]] = 1
        else:
            answ[spis[i]] += 1
    num = 0
    for i in answ.keys():
        if answ[i] > num:
            num = answ[i]
            key = i
        if answ[i] == num:
            if len(i) < len(key):
                num = answ[i]
                key = i
    return key


j = func('df skgzlrsl? jsr ghz ghz fs fs')
print(j)