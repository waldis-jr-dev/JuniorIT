from typing import Generator


def prime_numbers() -> Generator[int, None, None]:
    primes = []
    num = 2
    isprime = True
    while True:
        for prime in primes:
            if num % prime == 0:
                isprime = False
                break
        if isprime:
            primes.append(num)
            yield num
        num += 1


gen = prime_numbers()
while True:
    print(next(gen))
