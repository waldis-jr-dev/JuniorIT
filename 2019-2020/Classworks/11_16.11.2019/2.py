a = input('Enter:')
for i in a:
    if i.isdigit() and int(i) % 3 == 0:
        print(i)