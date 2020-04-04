def f(st):
    new = ''
    new2 = ''
    for i in st:
        if i in 'AEIOUaeiou':
            new += i
        else:
            new2 += i
    st = new2 + new
    return st


st = input('Enter string: ')
print(f(st))
