
def fibo(number: int = 0) -> int:
    a = 0
    b = 1
    if number in (0, 1):
        return b
    for _ in range(number):
        c = a + b
        a = b
        b = c
    return b


def recursive_fibo(number: int = 0) -> int:
    if number in (0, 1):
        return 1
    return recursive_fibo(number - 1) + recursive_fibo(number)


print(fibo(8))
print(recursive_fibo(8))
