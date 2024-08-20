"""
Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def solution(triplet_sum):
    for a in range(1, triplet_sum):
        for b in range(a + 1, triplet_sum):
            c = triplet_sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return None


if __name__ == "__main__":
    triplet_sum = 1000

    print(solution(triplet_sum))
