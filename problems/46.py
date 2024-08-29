"""
Problem 46: Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime
and twice a square?
"""

from itertools import count
from math import isqrt

from helpers import is_prime


def is_goldbach_conjecture(number, primes):
    for n in range(1, isqrt(number) + 1):
        if number - 2 * n**2 in primes:
            return True
    return False


def solution():
    primes = {1, 2}
    for number in count(3, 2):
        if is_prime(number):
            primes.add(number)
        elif not is_goldbach_conjecture(number, primes):
            return number


if __name__ == "__main__":
    print(solution())
