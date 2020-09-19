# generator
a = (x for x in range(10))
for el in a:
    print(el)
# list comprehension
b = [x for x in range(10)]
print(b)
# dict comprehension
c = {x: x**x for x in range(10)}
print(c)
