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


def is_truncatable_prime(number):
    if not is_prime(number):
        return False

    number = str(number)
    for i in range(1, len(number)):
        if not is_prime(int(number[i:])) or not is_prime(int(number[:-i])):
            return False

    return True


def solution():
    I = []
    i = 10
    count = 0
    while count < 11:
        if is_truncatable_prime(i):
            I.append(i)
            count += 1
        i += 1
    return sum(I)


if __name__ == "__main__":
    # TODO This is very slow

    print(solution())
