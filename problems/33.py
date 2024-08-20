"""
Problem 33: Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
"""

from itertools import combinations
from fractions import Fraction
from math import prod


def get_non_trivial_fractions():
    numbers = set(range(10, 100)) - set(range(10, 100, 10))
    fractions = []
    for numerator, denominator in combinations(numbers, 2):
        for i in str(numerator):
            if i in str(denominator):
                reduced_numerator = int(str(numerator).replace(i, '', 1))
                reduced_denominator = int(str(denominator).replace(i, '', 1))
                if numerator / denominator == reduced_numerator / reduced_denominator:
                    fractions.append((numerator, denominator))
    return fractions


def solution():
    return prod(
        Fraction(*fraction)
        for fraction in get_non_trivial_fractions()
    ).denominator


if __name__ == "__main__":
    print(solution())
