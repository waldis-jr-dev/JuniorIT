
def fi():
    a = 1
    b = 1
    while True:
        c = a + b
        yield c
        a = b
        b = c


print(next(fi()))
print(next(fi()))
#print(fi())
