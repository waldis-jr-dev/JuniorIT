def test():
    ch = 1
    while True:
        data = yield ch
        if data:
            yield f'{data} : {ch}'
        if data == 'stop':
            return
        ch += 1

gen = test()
print(next(gen))
print(gen.send('kek'))
print(next(gen))
print(gen.send('kek'))