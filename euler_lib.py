# Common methods used among problems

import math


# Creates a list of all prime factors of n (with multiplicity)
def prime_factors(n):
    prime_factors = []

    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n = n / i

    if n > 2:
        prime_factors.append(n)

    return prime_factors


# Creates a list of all proper divisors of n (without multiplicity)
def proper_divisors(n):
    divisors = [1]

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return divisors


# Returns the sum of all proper divisors of n
def sum_of_divisors(n):
    total = 1
    primes = prime_factors(n)
    if len(primes) == 1:
        return 1
    p = 0
    while p < len(primes):
        e = primes.count(primes[p])
        total *= (math.pow(primes[p], e + 1) - 1) // (primes[p] - 1)
        p += e
    return int(total) - n


# Prime number generator
def prime_generator():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


# Generate the primes up and including n
def primes_below(n):
    primeList = []
    primes = prime_generator()
    for i in primes:
        if i <= n:
            primeList.append(i)
        else:
            primes.close()
    return primeList


# Generate the first n primes
def first_n_primes(n):
    primeList = []
    count = 0
    primes = prime_generator()
    for i in primes:
        if count < n:
            primeList.append(i)
            count += 1
        else:
            primes.close()
    return primeList


# Sums the first n numbers
def sum_first_n(n):
    sum = n * (n + 1) / 2
    return sum
