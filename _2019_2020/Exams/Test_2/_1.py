def f(st):
    new = ''
    for i in st:
        if i not in 'aoeiuAOEIU':
            new += i
    return new


st = input('Enter string: ')
print(f(st))