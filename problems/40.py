"""
Problem 40: Champernowne's Constant

An  irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12-th digit of the fractional part is 1.

If d(n) represents the n-th digit of the fractional part, find the value of the
following expression.

d(1) x d(10) x d(100) x d(1000) x d(10000) x d(100000) x d(1000000)
"""

from itertools import count


def solution():
    result = 1
    target_digits = [1, 10, 100, 1000, 10000, 100000, 1000000]
    current_digit = 0
    for number in count(1):
        for digit in str(number):
            current_digit += 1
            if current_digit in target_digits:
                result *= int(digit)
                if current_digit == 1000000:
                    return result


if __name__ == "__main__":
    print(solution())
