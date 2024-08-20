"""
Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def solution(number_of_digits):
    return max(
        i * j
        for i in range(10 ** number_of_digits)
        for j in range(10 ** number_of_digits)
        if str(i * j) == str(i * j)[::-1]
    )


if __name__ == "__main__":
    number_of_digits = 3

    print(solution(number_of_digits))
