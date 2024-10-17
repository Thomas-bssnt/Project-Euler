"""
Problem 52: Permuted Multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain
the same digits.
"""

from itertools import count


def solution():
    for number in count(1):
        if all(sorted(str(number)) == sorted(str(number * i)) for i in range(2, 7)):
            return number


if __name__ == "__main__":
    print(solution())
