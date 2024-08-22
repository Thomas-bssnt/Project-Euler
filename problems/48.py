"""
Problem 48: Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

NUMBER_OF_DIGITS = 10
LIMIT = 1000


def solution():
    sum_ = sum(i**i for i in range(1, LIMIT + 1))
    return str(sum_)[-NUMBER_OF_DIGITS:]


if __name__ == "__main__":
    print(solution())
