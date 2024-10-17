"""
Problem 56: Powerful Digit Sum

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite
their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the
maximum digital sum?
"""


def solution():
    return max(
        sum(int(digit) for digit in str(a**b)) for a in range(100) for b in range(100)
    )


if __name__ == "__main__":
    print(solution())
