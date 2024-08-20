"""
Problem 7: 10001st prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

from helpers import is_prime


def solution(ith):
    ith_prime_number = 0
    number = 0
    while ith_prime_number != ith:
        if is_prime(number):
            ith_prime_number += 1
        number += 1
    return number - 1


if __name__ == "__main__":
    ith = 10001

    print(solution(ith))
