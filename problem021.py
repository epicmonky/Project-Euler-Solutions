# Let d(n) be defined as the sum of proper divisors of n. If d(a) = b and d(b) = a, where a =/= b, then a and b are
# an amicable pair and each of a and b are called amicable numbers. For example, the proper divisors of 220 are 1, 2,
# 4, 5, 10, 11, 20, 22, 44, 55, and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71,
# and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import euler_lib


if __name__ == '__main__':
    amicables = 0
    for a in range(2, 10000):
        b = euler_lib.sum_of_divisors(a)
        if b > a:
            if euler_lib.sum_of_divisors(b) == a:
                print(a, b)
                amicables += a + b

    print(amicables)
