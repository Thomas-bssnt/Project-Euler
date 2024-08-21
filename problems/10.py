"""
Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from helpers import prime_numbers

BOUND = 2000000


def solution():
    return sum(prime_numbers(BOUND))


if __name__ == "__main__":
    print(solution())
