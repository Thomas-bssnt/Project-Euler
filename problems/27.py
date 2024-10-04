"""
Problem 27: Quadratic primes

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer
values 0 ≤ n ≤ 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 primes
for the consecutive values 0 ≤ n ≤ 79. The product of the coefficients, −79 and
1601, is −126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that
produces the maximum number of primes for consecutive values of n, starting with
n = 0.
"""

from itertools import count

from helpers import is_prime, prime_numbers


def prime_formula(n, a, b):
    return n**2 + a * n + b


def get_number_of_primes(a, b):
    for n in count():
        if not is_prime(prime_formula(n, a, b)):
            return n


def solution():
    """
    For n = 0, the formula reduces to b, thus b must be prime.
    """
    max_product = 0
    max_primes = 0
    for b in prime_numbers(1000):
        for a in range(-999, 1000):
            number_of_primes = get_number_of_primes(a, b)
            if number_of_primes > max_primes:
                max_primes = number_of_primes
                max_product = a * b
    return max_product


if __name__ == "__main__":
    print(solution())
