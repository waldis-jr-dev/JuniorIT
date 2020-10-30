a = input().split()
maximum = 0
element = None
for j in a:
    if a.count(j) > maximum:
        maximum = a.count(j)
        element = j

print(element)