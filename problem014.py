# The following iterative sequence is defined for the set of positive integers:
# n --> n / 2 (n is even)
# n --> 3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain?

sequence_lengths = {1: 1}


def collatz_length(n):
    if n in sequence_lengths:
        return sequence_lengths[n]

    if n % 2 == 0:
        sequence_lengths[n] = 1 + collatz_length(int(n / 2))
    else:
        sequence_lengths[n] = 2 + collatz_length((3 * n + 1) / 2)
    return sequence_lengths[n]


if __name__ == '__main__':
    maxTuple = (1, 1)
    for i in range(500000, 1000001):  # collatz(2k) = 1 + collatz(k) > collatz(k)
        length = collatz_length(i)
        if maxTuple[1] < length:
            maxTuple = (i, length)
    print(maxTuple)
