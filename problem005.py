# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import euler_lib
import math


# Yields the smallest number divisible by the numbers 1 through n
def smallest_number_divisible_through(n):
    product = 1
    primes = euler_lib.primes_below(n)

    for i in range(len(primes)):
        exponent = math.floor(math.log(n) / math.log(primes[i]))
        product = product * primes[i] ** exponent

    return product


if __name__ == '__main__':
    print(smallest_number_divisible_through(20))
