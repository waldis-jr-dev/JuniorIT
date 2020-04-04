summ = 0
for i in range(-10, 11):
    for u in range(-10, 11):
        try:
            summ += i/u
        except ZeroDivisionError as exe:
            pass
print(summ)