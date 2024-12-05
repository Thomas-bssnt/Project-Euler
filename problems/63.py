"""
Problem 63: Powerful Digit Counts

The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728 = 8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

from math import log


def solution():
    """
    Let's consider the number x^n.

    For x^n to have exactly n digits, it must satisfy the inequality:
    10^(n-1) <= x^n < 10^n

    From the right-hand side of the inequality:
    x^n < 10^n
    => x < 10
    Thus, x must lie within the range: 1 <= x < 10.

    From the left-hand side of the inequality:
    10^(n-1) < x^n
    => 0.1*10^n < x^n
    => log(0.1) + n*log(10) < n*log(x)
    => n < log(10) / (log(10)-log(x))
    Thus the max integer value of n is given by
    The maximum integer n is given by:
    n = ⌊log(10) / (log(10)-log(x))⌋.
    """

    return sum(int(log(10) / (log(10) - log(x))) for x in range(1, 10))


if __name__ == "__main__":
    print(solution())
