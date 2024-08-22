"""
Problem 32: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
1 through 5 pandigital.

The prodict 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

from itertools import permutations

"""
There are only two possibilities for 9-digit pandigital numbers (multiplicand, 
multiplier, product):
- (1, 4, 4)
- (2, 3, 5) 
The set is used because some products can be obtained in more than one way.
"""


def solution():
    digits = "123456789"
    pandigital_products = set()

    for p in permutations(digits):
        p = "".join(p)
        for i, j in [(1, 4), (2, 3)]:
            if int(p[:i]) * int(p[i : i + j]) == (product := int(p[i + j :])):
                pandigital_products.add(product)

    return sum(pandigital_products)


if __name__ == "__main__":
    print(solution())
