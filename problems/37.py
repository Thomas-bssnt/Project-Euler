"""
Problem 37: Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from helpers import is_prime


def is_left_truncatable(number):
    number_str = str(number)
    for i in range(1, len(number_str)):
        if not is_prime(int(number_str[i:])):
            return False
    return True


def is_right_truncatable(number):
    number_str = str(number)
    for i in range(1, len(number_str)):
        if not is_prime(int(number_str[:-i])):
            return False
    return True


def is_truncatable_prime(number):
    if not is_prime(number):
        return False

    return is_left_truncatable(number) and is_right_truncatable(number)


def solution():
    truncatable_primes = []
    number = 10
    count = 0
    while count < 11:
        if is_truncatable_prime(number):
            truncatable_primes.append(number)
            count += 1
        number += 1
    return sum(truncatable_primes)


if __name__ == "__main__":
    print(solution())
