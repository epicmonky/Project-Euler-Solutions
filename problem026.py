# A unit fraction contains 1 in the numerator.
# 1 / 6 = 0.1(6) = 0.1666666..., which has a 1-digit recurring cycle.

# Find the value of d < 1000 for which 1 / d contains the longest recurring cycle.


# Returns the length of the recurring cycle for d / n
def cycle_length(d, n):
    digits = []
    r = d % n
    while r != 0:
        digits.append(d // n)
        d = 10 * d
        r = d % n
    digits.append(d // n)
    return len(digits) - 1


if __name__ == '__main__':
    print(cycle_length(1, 3))
