a = list(range(1, 1000))
print(a)
a = [i*len(str(i)) for i in a if str(i)[-1] != '1' and i % 2 != 0]
print(a)
