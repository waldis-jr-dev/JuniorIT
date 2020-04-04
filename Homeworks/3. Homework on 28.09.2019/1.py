num = input("enter number:")
if len(num) != 3 :
    print("stypid")
else :
    num = int(num)
    if num % 10 == num // 100 :
        print("palindrom")
    else :
        print("ne palindrom")
