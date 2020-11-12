# A Pythagorean triplet is a set of three natural numbers a < b < c for which
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc.


def return_triplet(s):
    for a in range(3, s):
        for b in range(a + 1, s):
            c = s - a - b
            if a * a + b * b == c * c:
                return a, b, c


if __name__ == '__main__':
    product = 1
    for i in return_triplet(1000):
        product = product * i
    print(product)
