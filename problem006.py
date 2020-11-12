# The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and
# the square of the sum is 3025 - 385 = 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

import euler_lib


# Returns the sum of the squares of the first n numbers
def sum_of_squares(n):
    sum = (2 * n + 1) * (n + 1) * n / 6
    return sum


if __name__ == '__main__':
    sum = euler_lib.sum_first_n(100)
    sum_sq = sum_of_squares(100)

    print(sum ** 2 - sum_sq)
