"""
Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from helpers import prime_numbers


def solution(bound):
    return sum(prime_numbers(bound))


if __name__ == "__main__":
    bound = 2000000

    print(solution(bound))
