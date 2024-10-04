"""
Problem 23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

from math import isqrt


def get_proper_divisors(number: int) -> list[int]:
    """
    Returns the proper divisors of the given number.
    """

    divisors = [1]
    for i in range(2, isqrt(number) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    return divisors


def get_proper_divisors_sum(bound):
    proper_divisors_sum = [0] * bound
    for number in range(1, bound):
        for multiple in range(2 * number, bound, number):
            proper_divisors_sum[multiple] += number
    return proper_divisors_sum


def is_abundant(number):
    return sum(get_proper_divisors(number)) > number


def solution():
    sum_ = 0

    abundant_numbers = set()
    for number in range(1, 28124):
        if is_abundant(number):
            abundant_numbers.add(number)

        for abundant_number in abundant_numbers:
            if number - abundant_number in abundant_numbers:
                break
        else:
            sum_ += number

    return sum_


if __name__ == "__main__":
    print(solution())
