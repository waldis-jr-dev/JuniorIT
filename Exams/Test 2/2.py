def f(st):
    summ = 0
    for i in st:
        if i.isdigit():
            i = int(i)
            summ += i
    return summ


st = input('Enter string: ')
print(f(st))
