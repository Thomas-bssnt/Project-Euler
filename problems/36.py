"""
Problem 36: Double-base palindromes

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
bases 10 and 2.

NOTE: The palindromic number, in either base, may not include leading zeros.
"""

from helpers import is_palindrome

LIMIT = 1000000


def solution():
    return sum(
        number
        for number in range(LIMIT)
        if is_palindrome(number) and is_palindrome(f"{number:b}")
    )


if __name__ == "__main__":
    print(solution())
