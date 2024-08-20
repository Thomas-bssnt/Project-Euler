"""
Problem 16: Power digit sum

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def solution(power):
    return sum(int(digit) for digit in str(2 ** power))


if __name__ == "__main__":
    power = 1000

    print(solution(power))
