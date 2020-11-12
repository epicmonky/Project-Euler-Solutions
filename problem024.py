# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
# 1, 2, 3, and 4. If all of the permutation are listed numerically, we call it lexicographical order.
# The lexicographical permutations of 0, 1, and 2 are: 012, 021, 102, 120, 201, 210

# What is the millionth lexicographical permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9?

import itertools


if __name__ == '__main__':
    digits = list(range(10))

    perms = list(itertools.permutations(digits))

    number = ""
    for i in perms[1000000 - 1]:
        number += str(i)
    print(number)
