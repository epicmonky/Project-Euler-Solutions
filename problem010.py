# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

# Find the sum of all the primes below 2 million.

import euler_lib

if __name__ == '__main__':
    primes = euler_lib.primes_below(2000000)
    print(sum(primes))
