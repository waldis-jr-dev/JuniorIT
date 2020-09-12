number = input("enter string:")
if len(number) % 2 == 0 :
    b = number[ : : -1 ]
    print(b)
else :
    b = number[ : 3 : 1]
    print(b)

