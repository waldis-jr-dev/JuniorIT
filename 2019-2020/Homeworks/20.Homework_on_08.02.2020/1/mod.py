def e(num):
    indt = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            indt = False
            break
    return indt
