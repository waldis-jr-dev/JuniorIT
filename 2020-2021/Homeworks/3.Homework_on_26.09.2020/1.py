a = list(range(-1000, 0))
a = [i**2 - 2*len(str(i)) for i in a if str(i)[-2] != '7' and sum(map(int, str(i)[1::])) >= i]
print(a)
