def count_element(pi):
    answ = []
    for i in range(0, 10):
        answ.append([i, 0])
    with open(pi, 'r') as file:
        for i in file:
            i = i.strip()
            for j in i:
                if j.isdigit():
                    j = int(j)
                    answ[j][1] +=  1
    return answ


print(count_element('pi.txt'))