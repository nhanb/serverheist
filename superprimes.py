import sys


# https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
def primes_sieve(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


def is_super_prime(num: int, is_prime_func) -> bool:
    remainder = num
    while True:
        if not is_prime_func(remainder):
            return False
        remainder = num // 10
        if remainder == 0:
            break
        num = remainder
    return True


def findSuperPrime(n):
    if n <= 2:
        return []

    primes = set(primes_sieve(n))

    def is_prime2(num):
        return num in primes

    return sorted(prime for prime in primes if is_super_prime(prime, is_prime2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python superprimes.py 100")

    print(findSuperPrime(int(sys.argv[1])))
