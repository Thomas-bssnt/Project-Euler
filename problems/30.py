"""
Problem 30: Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
"""

POWER = 5


def solution():
    """
    A number with at least n digits will be always greater than the sum of the
    powers
    """
    n = 1
    while 9**POWER * n >= 10**n - 1:
        n += 1

    return sum(
        number
        for number in range(3, 10**n)
        if number == sum(int(digit) ** POWER for digit in str(number))
    )


if __name__ == "__main__":
    print(solution())
