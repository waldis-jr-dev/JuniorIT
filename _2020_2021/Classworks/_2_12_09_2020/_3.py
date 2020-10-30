def years():
    is_even = True
    year = 2000
    while True:
        data = yield year
        if data == 'odd' and is_even:
            year -= 1
            is_even = False
        if data == 'even' and not is_even:
            year -= 1
            is_even = True
        year += 2


gen = years()
print(next(gen))
print(next(gen))
print(gen.send('odd'))
print(next(gen))
print(next(gen))
print(gen.send('even'))
print(next(gen))
print(next(gen))
