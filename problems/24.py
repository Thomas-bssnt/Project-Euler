"""
Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3, and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexiographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""

from itertools import permutations

NUMBERS = "0123456789"
INDEX = 1000000


def solution():
    return int("".join(list(permutations(NUMBERS))[INDEX - 1]))


if __name__ == "__main__":
    print(solution())

    # No need to sort as permutations return in the right order already
