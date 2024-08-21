"""
Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

from helpers import is_prime

NUMBERS = list(range(1, 21))


def solution():
    result = 1
    for number in NUMBERS:
        if is_prime(number):
            power = 1
            while number ** power <= max(NUMBERS):
                result *= number
                power += 1
    return result


if __name__ == "__main__":
    print(solution())
