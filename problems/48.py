"""
Problem 48: Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


def solution(number_of_digits, bound):
    sum_ = sum(i ** i for i in range(1, bound + 1))
    return str(sum_)[-number_of_digits:]


if __name__ == "__main__":
    number_of_digits = 10
    bound = 1000

    print(solution(number_of_digits, bound))
