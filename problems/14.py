"""
Problem 14: Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is enough to
state that it is a sequence of 11 terms. Although it has not been proved yet
(Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from functools import cache

LIMIT = 1000000


@cache
def collatz_sequence_length(number):
    if number == 1:
        return 1
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    return collatz_sequence_length(number) + 1


def solution():
    return max(range(1, LIMIT), key=collatz_sequence_length)


if __name__ == "__main__":
    print(solution())
