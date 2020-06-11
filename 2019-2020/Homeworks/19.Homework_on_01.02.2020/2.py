def f(n, m):
    if n > m:
        k = n
    else:
        k = m
    while k != 1:
        if n % k == 0 and m % k == 0:
            return [n//k, m//k]
        else:
            k -= 1
    return [n,m]

n = int(input('Enter first: '))
m = int(input('Enter second: '))

print(f(n, m))