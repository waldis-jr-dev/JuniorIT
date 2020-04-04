a = [2, None, 5, None, 7]
func = lambda x: 0 if x == None else x
for i in a:
    print(func(i))