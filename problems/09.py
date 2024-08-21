"""
Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""

TRIPLET_SUM = 1000


def solution():
    for a in range(1, TRIPLET_SUM):
        for b in range(a + 1, TRIPLET_SUM):
            c = TRIPLET_SUM - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return None


if __name__ == "__main__":
    print(solution())
