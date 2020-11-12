# n! means n x (n - 1) x ... x 3 x 2 x 1
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import math


def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s


if __name__ == '__main__':
    n = math.factorial(100)
    print(sum_of_digits(n))
