def f(num, first, l):
    if num == 1:
        return first
    return l*f(num-1, first, l)


num = int(input('num = '))
first = int(input('first = '))
l = int(input('l = '))
print(f(num, first, l))
