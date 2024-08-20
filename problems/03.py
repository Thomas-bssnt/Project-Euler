"""
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from helpers import prime_factorization


def solution(number_to_factorize):
    return max(prime_factorization(number_to_factorize))


if __name__ == "__main__":
    number_to_factorize = 600851475143

    print(solution(number_to_factorize))
