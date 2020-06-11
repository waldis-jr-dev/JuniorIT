def f(n, m):
    k = max(n, m)
    while k != 1:
        if n % k == 0 and m % k == 0:
            return [n//k, m//k]
        else:
            k -= 1
    return [n,m]
