def f(num):
    new = ''
    with open('pi.txt', 'r') as file:
        for i in file:
            i.strip()
            new += i

    return num in new


num = input('Num: ')
print(f(num))
