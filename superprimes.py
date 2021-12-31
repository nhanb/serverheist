import sys
from functools import lru_cache


# https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
def primes_sieve(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


# https://stackoverflow.com/questions/4114167/checking-if-a-number-is-prime-in-python
@lru_cache(maxsize=None)
def is_prime(n):
    result = n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
    # print(f'{n} is{"" if result else " NOT"} prime')
    return result


@lru_cache(maxsize=None)
def is_super_prime(num: int) -> bool:
    remainder = num
    while True:
        if not is_prime(remainder):
            return False
        remainder = num // 10
        if remainder == 0:
            break
        num = remainder
    return True


def findSuperPrime(n):
    return [prime for prime in range(n + 1) if is_super_prime(prime)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python superprimes.py 100")

    print(findSuperPrime(int(sys.argv[1])))
