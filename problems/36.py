"""
Problem 36: Double-base palindromes

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
bases 10 and 2.

NOTE: The palindromic number, in either base, may not include leading zeros.
"""


def solution(bound):
    return sum(
        number
        for number in range(bound)
        if (str(number) == str(number)[::-1] and f"{number:b}" == f"{number:b}"[::-1])
    )


if __name__ == "__main__":
    bound = 1000000

    print(solution(bound))
