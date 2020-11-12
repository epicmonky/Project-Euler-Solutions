# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 x 99

# Find the largest palindrome made from the product of two 3-digit numbers.

# Returns the decimal reverse of n (i.e. 123 -> 321)
def reverse(n):
    reversed = 0
    while n > 0:
        reversed = 10 * reversed + n % 10
        n = int(n / 10)
    return reversed


# Checks if n is palindromic
def is_palindromic(n):
    return n == reverse(n)


# Removes non-palindromic numbers
def get_palindromes(elements):
    i = 0
    while i < len(elements):
        if not is_palindromic(elements[i]):
            elements.pop(i)
            i -= 1
        i += 1


if __name__ == '__main__':
    products = []
    for x in range(100, 1000):
        for y in range(x, 1000):
            products.append(x * y)

    get_palindromes(products)
    print(max(products))
