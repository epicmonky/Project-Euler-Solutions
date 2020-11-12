# Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20 x 20 grid?


import math


def num_routes(m, n):
    num = int(math.factorial(m + n) / (math.factorial(m) * math.factorial(n)))
    return num


if __name__ == '__main__':
    print(num_routes(20, 20))
