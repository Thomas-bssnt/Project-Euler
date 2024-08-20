"""
Problem 35: Circular primes

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from helpers import prime_numbers


def cyclic_permutations(number):
    number = str(number)
    for i in range(len(number)):
        yield int(number[i:] + number[:i])


def solution():
    bound = 1000000

    prime_numbers = set(prime_numbers(bound))

    return sum(
        1
        for prime in prime_numbers
        if set(cyclic_permutations(prime)).issubset(prime_numbers)
    )


if __name__ == "__main__":
    print(solution())
