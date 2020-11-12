# A perfect number is a number equal to the sum of its proper divisors. For example, 28 = 1 + 2 + 4 + 7 + 14
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant
# if this sum exceeds n. As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that
# can be be written as the sum of two abundant numbers is 24. By analysis, it can be shown that all integers
# greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be
# reduced any further even though it is known that the greatest number that cannot be expressed as the sum of two
# abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import euler_lib


# Checks if n is abundant
def is_abundant(n):
    if euler_lib.sum_of_divisors(n) > n:
        return True
    else:
        return False


if __name__ == '__main__':
    nums = [False] * 28124

    abundants = []
    for i in range(12, 28123):
        if is_abundant(i):
            # print(i)
            abundants.append(i)

    print(len(abundants))

    for a in range(len(abundants)):
        for b in range(a, len(abundants)):
            total = abundants[a] + abundants[b]
            if total > 28123:
                break
            elif nums[total]:
                continue
            else:
                print(a, b, total)
                nums[total] = True

    answer = 0
    for i in range(len(nums)):
        if not nums[i]:
            answer += i

    print(answer)
