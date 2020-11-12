# The Fibonacci sequence is defined by the recurrence relation:
# F_n = F_{n-1} + F_{n-2}

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math


# Generates the n-th Fibonacci number using the generating function
# def fibonacci(n):
#     x = 1 / math.sqrt(5) * math.pow(((1 + math.sqrt(5)) / 2), n)
#     y = 1 / math.sqrt(5) * math.pow(((1 - math.sqrt(5)) / 2), n)
#
#     return round(x - y)


if __name__ == '__main__':
    fib = [1, 1]
    index = 3  # Ignores first 2 elements, so this breaks if len == 1
    while True:
        Fn = fib[0] + fib[1]
        if len(str(Fn)) == 1000:
            break
        else:
            fib[0] = fib[1]
            fib[1] = Fn
            index += 1

    print(index, Fn)
