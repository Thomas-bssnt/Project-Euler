from itertools import permutations

"""
There are only two possibilities for 9-digit pandigital numbers (multiplicand, multiplier, product):
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
            if int(p[:i]) * int(p[i:i + j]) == (product := int(p[i + j:])):
                pandigital_products.add(product)

    return sum(pandigital_products)


if __name__ == "__main__":
    print(solution())
