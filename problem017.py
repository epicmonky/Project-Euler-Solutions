# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.

# If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used?

name_length = {
    1: 3,  # one
    2: 3,  # two
    3: 5,  # three
    4: 4,  # four
    5: 4,  # five
    6: 3,  # six
    7: 5,  # seven
    8: 5,  # eight
    9: 4,  # nine
    10: 3,  # ten
    11: 6,  # eleven
    12: 6,  # twelve
    13: 8,  # thirteen
    14: 8,  # fourteen
    15: 7,  # fifteen
    16: 7,  # sixteen
    17: 9,  # seventeen
    18: 8,  # eighteen
    19: 8,  # nineteen
    20: 6,  # twenty
    30: 6,  # thirty
    40: 5,  # forty
    50: 5,  # fifty
    60: 5,  # sixty
    70: 7,  # seventy
    80: 6,  # eighty
    90: 6,  # ninety
    100: 7  # hundred

}


def get_length(num):
    total_length = 0
    if num >= 1000:
        x = num // 1000
        total_length += name_length[x]
        total_length += 8

        num = num % 1000

    if num >= 100:
        x = num // 100
        total_length += name_length[x]
        total_length += 7

        num = num % 100
        if num > 0:
            total_length += 3
    if num > 20:
        x = num // 10
        total_length += name_length[x * 10]
        num = num % 10
    #   print(num)
    if num > 0:
        total_length += name_length[num]

    return total_length


if __name__ == '__main__':
    total_length = 0
    for i in range(1, 1001):
        current_length = get_length(i)
        total_length += current_length

    print(total_length)
