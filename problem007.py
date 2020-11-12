# By listing te first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import euler_lib

if __name__ == '__main__':
    primes = euler_lib.first_n_primes(10001)
    print(primes[-1])
