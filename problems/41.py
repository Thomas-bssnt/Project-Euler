"""
Problem 41: Pandigital prime

We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations
from helpers import is_prime


def solution():
    """
    digits is equal to "987654321" and not "123456789" so that permutations are
    generated in descending order.
    """
    digits = "987654321"
    while digits:
        digits = digits[1:]
        for permutation in permutations(digits):
            number = int("".join(permutation))
            if is_prime(number):
                return number


if __name__ == "__main__":
    print(solution())
