"""
Problem 21: Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and
b are amicable.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from helpers import sum_proper_divisors

LIMIT = 10000


def is_amicable(number):
    d_number = sum_proper_divisors(number)
    return d_number != number and number == sum_proper_divisors(d_number)


def solution():
    return sum(number for number in range(LIMIT) if is_amicable(number))


if __name__ == "__main__":
    print(solution())
