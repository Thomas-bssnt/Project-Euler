"""
Problem 47: Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5.

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""

from helpers import prime_factorization
from itertools import count


def solution():
    consecutive_count = 0
    for number in count(1):
        if len(set(prime_factorization(number))) == 4:
            consecutive_count += 1
            if consecutive_count == 4:
                return number - 3
        else:
            consecutive_count = 0


if __name__ == "__main__":
    print(solution())
