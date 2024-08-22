"""
Problem 34: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

NOTE: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial


def solution():
    """
    A number with at least n digits will be always greater than the sum of the
    factorial of its digits.
    """
    factorials = {str(number): factorial(number) for number in range(10)}

    n = 1
    while factorials["9"] * n >= 10**n - 1:
        n += 1

    return sum(
        number
        for number in range(3, 10**n)
        if sum(factorials[digit] for digit in str(number)) == number
    )


if __name__ == "__main__":
    print(solution())
