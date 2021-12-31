# https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python
def primes_sieve(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


def is_super_prime(num: int) -> bool:
    pass
