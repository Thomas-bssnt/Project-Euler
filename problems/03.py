"""
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from helpers import prime_factorization

NUMBER_TO_FACTORIZE = 600851475143


def solution():
    return max(prime_factorization(NUMBER_TO_FACTORIZE))


if __name__ == "__main__":
    print(solution())
